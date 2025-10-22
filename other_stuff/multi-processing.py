"""
This script demonstrates the use of the multiprocessing module in Python.
Objective:
----------
To create multiple worker processes that perform tasks concurrently and log their activities.

What did we learn?
------------------
Logging settings are not inherited by child processes in Python's multiprocessing module.
You will need to set up logging in each worker process to ensure that logs are captured correctly.

How to capture the process id in the log file?
-------------------------------------------------
See the logging format in the setup_logging function, which includes the process id (%(process)d).
The process id gives us a sense of which worker is logging what information.

"""
import logging
import time
from multiprocessing import Pool


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        filename=r"c:\truetemp\anypython-app.log",
        filemode="a",
        format="%(asctime)s-%(levelname)s-%(process)d-%(message)s"
    )


def worker(name):
    setup_logging()  # Ensure logging is set up in each worker
    logging.info(f"Worker {name} started")
    print(f"Worker {name} is doing some work...")
    time.sleep(2)
    logging.info(f"Worker {name} finished")
    print(f"Worker {name} has completed its task")
    return f"Result from worker:{name}"


def start_workers():
    names = [f"Worker-{i+1}" for i in range(15)]
    with Pool(processes=3) as pool:
        results = pool.map(worker, names)
    logging.info(f"Results: {results}")
    logging.info("All workers finished")
    logging.info("---------------------------")


if __name__ == "__main__":
    setup_logging()
    logging.info("*********")
    logging.info("Main Script started")
    start_workers()
