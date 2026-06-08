"""
In the following example we are trying to acquire an exclusive lock on a file. 

Option 1
--------
We cannot use fcntl on Windows, so this code will only work on Unix-like systems.
Error:
    No module named 'fcntl'
https://stackoverflow.com/questions/1422368/fcntl-substitute-on-windows

Option 2
--------
FileLock from the filelock library is a cross-platform solution that works on both Unix and Windows. 
It creates a separate lock file to manage access to the resource, ensuring that only one process can access it at a time.
The original file remains unlocked, allowing other processes to read it while one process is writing to it.
It is a convention for other processes to check for the existence of the lock file before accessing the resource, 
but it does not prevent them from doing so if they ignore this convention.

"""
import time
import os


def demo_unix_only(file_path: str) -> None:
    import fcntl
    with open(file_path, "w") as f:
        print("Trying to acquire lock...")
        fcntl.flock(f, fcntl.LOCK_EX)
        print("Lock acquired. Doing some work...")
        time.sleep(5)
        print("Releasing lock.")
        fcntl.flock(f, fcntl.LOCK_UN)


def demo_cross_platform(file_path: str) -> None:
    from filelock import FileLock
    lock = FileLock(file_path + ".lock")
    with lock:
        print("Lock acquired. Doing some work...")
        time.sleep(5)
        print("Releasing lock.")


if __name__ == "__main__":
    demo_file = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "readme.md")
    print(f"Using file: {demo_file}")
    # demo_unix_only(file_path=demo_file)
    demo_cross_platform(file_path=demo_file)
