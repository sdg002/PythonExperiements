[[_TOC_]]]

# About

How to lock a file in Python? **Short answer** - you follow different approaches depending on the underlying operating system

# Lessons learnt

You can place a lock on a file using msvcrt. You can read/write to the file. However, you cannot move/delete the file it is locked. You will have to come out of the `open` block or explicitly unlock using msvcrt to do the move/delete operation

# Next steps

We know we cannot delete/move while file is locked. Can we copy the contents to a file with the same name in another directory? And erase the contents while the file handle is still open. Thus we get a file whic his zero bytes in length,i.e. not much of any significance

# 1-Response from Copilot

I asked Copilot this question:

## Question

Tell me how msvcrt can be helpful in locking a file in Winodws Server environment, so that multile processes from 2 or more computers trying to consume files form a central network directory in a first in first out manner and subsequently move to a central archive folder - do not end up reading the same file.

## Short answer

`msvcrt.locking` **can** work across machines on a Windows file share, because it maps to Windows byte‑range locks (`LockFile`/`LockFileEx`) that the SMB server enforces centrally. But for your exact scenario — multiple machines pulling files FIFO from a central directory and moving them to an archive — **locking alone is the wrong primitive**. The robust mechanism is an **atomic rename/move to claim the file**. Use the lock (optionally) only while reading.

Here's the reasoning and the pattern.

## Why pure locking is fragile here

1. **A lock only lives as long as the open handle.** `msvcrt.locking` locks a byte range on an _open file_. To move the file you must `shutil.move` it — but `move` across the tree is a rename, and you cannot hold a byte lock and rename the file in one atomic step. There's a window where the file is unlocked but not yet claimed, so two machines can race.

2. **`_locking` is always exclusive — there is no shared read lock.** In the Microsoft C runtime that backs `msvcrt`, `LK_RLCK`/`LK_NBRLCK` are **the same as** `LK_LOCK`/`LK_NBLCK` (exclusive). So your comment "shared lock for reading" in `msvcrt002.py` is misleading — it's actually exclusive, which is fine for your goal, but don't rely on shared‑read semantics.

3. **Locking gives you no FIFO ordering.** Byte‑range locks say nothing about _which_ file is next. Ordering must come from you (sort by creation/modified time).

4. **SMB lock caveats.** Byte‑range locks over SMB are enforced by the server, but behavior around dropped connections, lock recovery after a network blip, and opportunistic locking/caching can surprise you. It works, but it's not the cleanest contract for "claim this item exactly once."

## The reliable pattern: claim-by-atomic-move

On a single volume/share, **rename is atomic and the OS guarantees only one caller wins**. Turn "may I process this file?" into "can I rename it into my private in‑progress area?":

```
central_incoming/   <- producers drop files here
processing/         <- (optional) per-machine/PID claim area
archive/            <- final destination
```

Per worker loop:

1. List `central_incoming`, **sort by creation/mtime** (FIFO).
2. For the oldest file, attempt an **atomic move** to a unique name you own, e.g. `processing/<host>-<pid>-<name>`.
   - If the move **succeeds**, you own it — no one else can now get it.
   - If it **fails** (file gone / already moved), another worker won it — skip to the next file.
3. Process/read your claimed copy.
4. Move it to `archive/`.

```python
import os
import socket
import pathlib as plib

def claim_and_process(incoming: plib.Path, processing: plib.Path, archive: plib.Path) -> None:
    processing.mkdir(exist_ok=True)
    archive.mkdir(exist_ok=True)

    files = sorted(
        (f for f in incoming.iterdir() if f.is_file()),
        key=lambda p: p.stat().st_ctime,  # FIFO by creation time
    )

    tag = f"{socket.gethostname()}-{os.getpid()}"
    for src in files:
        claimed = processing / f"{tag}-{src.name}"
        try:
            os.rename(src, claimed)  # atomic claim; raises if someone else took it
        except (FileNotFoundError, PermissionError, FileExistsError, OSError):
            continue  # lost the race, try the next file

        # We exclusively own `claimed` now.
        with open(claimed, "r", encoding="utf-8") as fh:
            data = fh.read()
        # ... process data ...

        os.replace(claimed, archive / src.name)  # atomic finalize
```

Key rules that make this safe across machines:

- **Keep every directory on the same share/volume** so `os.rename`/`os.replace` stay atomic (a cross‑volume move degrades to copy+delete and loses atomicity).
- Give each claim a **unique destination name** (`host-pid-...`) so two winners can never collide.
- Treat any rename failure as "someone else got it" and move on.

## Where `msvcrt.locking` still helps

- If **producers might still be writing** a file when workers scan, add an exclusive `msvcrt.locking` check to skip files that are open for writing.
- Or better, have producers write to a temp name and `os.rename` into `central_incoming` only when complete — then presence in the folder means "ready," and you don't need a lock at all.

## Recommendation for your code

Your `msvcrt002.py` currently: opens → locks → sleeps → unlocks → then `shutil.move`. The unlock‑then‑move gap is the race window on a multi‑machine share. Switch the claim mechanism to **atomic rename first, then read, then archive**, and keep the msvcrt lock only as an optional "is the producer still writing?" guard.

# 2-Response from Copilot

## Question

I am in a Windows server environment. I have multiple processes from 2 or more computers trying to read files from a central network directory in a first in first out manner and subsequently move to a central archive folder. No single file should be read concurrently by 2 or more processes. Can you recommend a Python based solution.

## Recommendation: claim-by-atomic-rename (don't use locks for mutual exclusion)

For "read from a central share, FIFO, exactly one process per file, then archive," the most
reliable Windows/SMB approach is **not** file locking — it is an **atomic rename to claim
ownership**. On a single SMB volume, `rename` is atomic and only one caller can win. That single
guarantee gives you mutual exclusion for free, and it works across machines because the file
server arbitrates it.

### Directory layout (all on the same share/volume so renames stay atomic)

```
\\server\share\incoming\      producers drop finished files here
\\server\share\processing\    per-worker claim area (winner-only)
\\server\share\archive\       final destination
\\server\share\failed\        poison-message quarantine
```

### Core rules

1. **FIFO** = sort candidates by creation/modified time before claiming.
2. **Claim** = `os.rename(incoming/f -> processing/<host>-<pid>-<f>)`. Success = you own it;
   failure = someone else got it, move on.
3. **Finalize** = `os.replace(processing/... -> archive/f)`.
4. **Producers** write to a temp name then rename into `incoming/`, so a file's mere presence
   means "complete and ready" (avoids reading half-written files).

### Why not `msvcrt.locking` for mutual exclusion?

- A byte-range lock only lives while the handle is open; there is an unlocked window before you
  move the file where a second machine can grab it.
- `_locking` is always exclusive (no shared read lock) and gives you no FIFO ordering.
- Rename is a single atomic operation with a clean "exactly one winner" contract — simpler and
  safer than lock + move.

### Reference implementation

```python
"""FIFO, single-consumer-per-file processor for a shared Windows directory.

Multiple instances of this script may run on multiple machines against the same
UNC share. Mutual exclusion is achieved by an atomic rename ("claim"), not locks.
Keep incoming/processing/archive/failed on the SAME volume so renames stay atomic.
"""
import os
import socket
import time
import logging
import pathlib as plib


WORKER_TAG = f"{socket.gethostname()}-{os.getpid()}"


def _fifo_candidates(incoming: plib.Path) -> list[plib.Path]:
    """Return regular files oldest-first (FIFO by creation time)."""
    files = [f for f in incoming.iterdir() if f.is_file()]
    files.sort(key=lambda p: p.stat().st_ctime)
    return files


def _try_claim(src: plib.Path, processing: plib.Path) -> plib.Path | None:
    """Atomically claim `src` by renaming it into `processing`.

    Returns the claimed path on success, or None if another worker won the race
    (or the file vanished / is still being written and is momentarily locked).
    """
    claimed = processing / f"{WORKER_TAG}-{src.name}"
    try:
        os.rename(src, claimed)  # atomic on a single volume; only one winner
        return claimed
    except (FileNotFoundError, PermissionError, FileExistsError, OSError):
        return None


def _process_one(claimed: plib.Path) -> None:
    """Do the real work for a claimed file. Replace with your own logic."""
    with open(claimed, "r", encoding="utf-8") as fh:
        _ = fh.read()
    # ... business logic here ...


def run_worker(
    incoming: plib.Path,
    processing: plib.Path,
    archive: plib.Path,
    failed: plib.Path,
    poll_seconds: float = 1.0,
) -> None:
    for d in (processing, archive, failed):
        d.mkdir(parents=True, exist_ok=True)

    logging.info("Worker %s started, watching %s", WORKER_TAG, incoming)
    while True:
        did_work = False
        for src in _fifo_candidates(incoming):
            claimed = _try_claim(src, processing)
            if claimed is None:
                continue  # lost the race or not ready; try the next file

            did_work = True
            logging.info("Claimed %s", src.name)
            try:
                _process_one(claimed)
                os.replace(claimed, archive / src.name)  # atomic finalize
                logging.info("Archived %s", src.name)
            except Exception:
                logging.exception("Failed processing %s; quarantining", src.name)
                os.replace(claimed, failed / src.name)  # don't reprocess poison files

        if not did_work:
            time.sleep(poll_seconds)  # idle back-off


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    base = plib.Path(r"\\server\share")
    run_worker(
        incoming=base / "incoming",
        processing=base / "processing",
        archive=base / "archive",
        failed=base / "failed",
    )
```

### Operational notes

- **Same volume for all folders.** A cross-volume `os.rename`/`os.replace` degrades to copy+delete
  and loses atomicity. Keep everything under one share.
- **Crash recovery.** If a worker dies mid-processing, its file is stranded in `processing\` under
  that worker's `host-pid` tag. Add a janitor that, on startup, re-queues stale files whose tag
  matches this host/pid, or that are older than a timeout.
- **Producers.** Have producers write `foo.txt.tmp` then rename to `foo.txt`. Presence in
  `incoming\` then reliably means "complete."
- **Scaling / ordering caveat.** Strict global FIFO across many concurrent workers is best-effort:
  the oldest file is _attempted_ first, but a faster worker may claim a slightly newer file while
  another is mid-claim. If you need strict, ordered, once-only delivery at higher volume, consider
  a real queue (MSMQ, RabbitMQ, Azure Service/Storage Queue) with the share used only for payloads.
- **No third-party libraries required** — this uses only the standard library and the OS's atomic
  rename guarantee.
