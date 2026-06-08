"""
Demonstrate locking a file region on Windows using msvcrt.locking.

Run this script in two terminals at the same time. The first process acquires
the lock and holds it for a few seconds. The second process retries until the
lock is released.
"""

import msvcrt
import os
import time
from pathlib import Path


def lock_file_demo(file_path: Path, hold_seconds: int = 10) -> None:
    """Try to acquire an exclusive lock on the first byte of a file.

    Args:
            file_path: Path to the file to lock.
            hold_seconds: Seconds to keep the lock once acquired.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Open for read/write in binary mode. File must exist for msvcrt locking.
    with open(file_path, "a+b") as file_obj:
        file_obj.seek(0, os.SEEK_SET)
        file_obj.write(b"0")
        file_obj.flush()

        # Lock exactly 1 byte from current pointer (offset 0).
        lock_length = 1
        print(f"PID {os.getpid()}: trying to lock {file_path}")

        while True:
            try:
                file_obj.seek(0, os.SEEK_SET)
                msvcrt.locking(file_obj.fileno(), msvcrt.LK_NBLCK, lock_length)
                print(f"PID {os.getpid()}: lock acquired")
                break
            except OSError:
                print(
                    f"PID {os.getpid()}: file is locked by another process, retrying...")
                time.sleep(1)

        try:
            print(f"PID {os.getpid()}: holding lock for {hold_seconds} seconds")
            time.sleep(hold_seconds)
        finally:
            file_obj.seek(0, os.SEEK_SET)
            msvcrt.locking(file_obj.fileno(), msvcrt.LK_UNLCK, lock_length)
            print(f"PID {os.getpid()}: lock released")


if __name__ == "__main__":
    lock_file_demo(Path("msvcrt001.lock"), hold_seconds=10)
