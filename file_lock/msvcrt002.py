"""
About this script
This script demonstrates how to use file locking in Python on Windows using the msvcrt module.
It scans a directory for text files, locks them for reading, and then moves them to an output directory.

How to run this script:
1. Open two terminal windows.
2. Generate lots of text files in the scan_dir directory (e.g., copy some existing text file multiple times).
3. Run this script in both terminal windows at the same time.
The first process will acquire locks on the files and move them to the "out" directory.

"""
import msvcrt
import pathlib as plib
import logging
import shutil
import time


def read_first_available_file(scan_folder: plib.Path, out_folder: plib.Path) -> None:
    """
    Read the first line of a file with a shared lock.
    Move the file to a "processed" subdirectory after reading.
    """
    processed_dir = out_folder
    processed_dir.mkdir(exist_ok=True)

    list_of_files_process: list[plib.Path] = []
    for some_file in scan_folder.iterdir():
        if not some_file.is_file():
            continue

        source_file_path = some_file
        processed_file_path = processed_dir / source_file_path.name
        should_move = False
        lock_acquired = False
        with open(source_file_path, "r", encoding="utf-8") as some_file_handle:
            # Lock the file for shared reading (non-blocking)
            try:
                msvcrt.locking(some_file_handle.fileno(), msvcrt.LK_NBRLCK, 1)
                lock_acquired = True
                logging.info(f"Locked file: {source_file_path.name}")
                logging.info(f"Reading from file: {source_file_path.name}")
                time.sleep(2)  # Simulate some processing time
                logging.info(f"Finished reading file: {source_file_path.name}")
                should_move = True
                list_of_files_process.append(source_file_path)
            except Exception as e:
                logging.error(
                    f"Error while processing file {source_file_path.name}: {e}", exc_info=True)
                continue
            finally:
                # Unlock the file
                if lock_acquired:
                    msvcrt.locking(some_file_handle.fileno(),
                                   msvcrt.LK_UNLCK, 1)

        if should_move:
            logging.info(
                f"Moving file '{source_file_path.name}' to '{processed_file_path}'")
            shutil.move(str(source_file_path), str(processed_file_path))
            logging.info(
                f"Moved file '{source_file_path.name}' to '{processed_file_path}'")
    logging.info(
        f"Finished scanning for files. Total files processed: {len(list_of_files_process)}")
    for f in list_of_files_process:
        logging.info(f"Processed file: {f.name}")


if __name__ == "__main__":
    # shutil.copy(
    #     r"C:\Users\saurabhd\MyTrials\Python\PythonExperiements\file_lock\scan_dir\New Text Document - Copy.txt",
    #     r"C:\Users\saurabhd\MyTrials\Python\PythonExperiements\file_lock\out\New Text Document - Copy.txt")
    # exit(1)
    scan_dir = plib.Path(__file__).parent / "scan_dir"
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    logging.info(f"Scanning directory: {scan_dir}")
    out_dir = plib.Path(__file__).parent / "out"
    read_first_available_file(scan_folder=scan_dir, out_folder=out_dir)
