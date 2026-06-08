"""Demonstrate lock and delete behavior on Windows with msvcrt.

Important: with normal Python file opens on Windows, deleting a file while it is
open/locked typically fails with PermissionError. The safe pattern is:
lock -> work -> unlock -> close -> delete.
"""

from __future__ import annotations

import msvcrt
import os
import pathlib as plib
import time


def lock_and_delete_demo(file_path: plib.Path, hold_seconds: int = 10) -> None:
    """Show delete attempt while locked, then delete after unlock/close."""
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w+b") as file_handle:
        file_handle.write(b"x")
        file_handle.flush()
        file_handle.seek(0)

        msvcrt.locking(file_handle.fileno(), msvcrt.LK_NBLCK, 1)
        print(f"Locked file: {file_path}")

        try:
            try:
                os.remove(file_path)
                print("Unexpected: file deleted while locked/open")
            except PermissionError as exc:
                print(
                    f"Expected on Windows: cannot delete while locked/open -> {exc}")

            print(f"Holding lock for {hold_seconds} seconds")
            time.sleep(hold_seconds)
        finally:
            msvcrt.locking(file_handle.fileno(), msvcrt.LK_UNLCK, 1)
            print(f"Unlocked file: {file_path}")

    # File is now closed; delete succeeds.
    os.remove(file_path)
    print(f"Deleted file after unlock/close: {file_path}")


if __name__ == "__main__":
    sample_file = plib.Path(__file__).parent / "scan_dir" / "sample.txt"
    lock_and_delete_demo(sample_file, hold_seconds=10)
