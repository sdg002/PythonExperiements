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
import os
import time
from multiprocessing import Pool


import logging
import sys
LOG_FILE = "c:\\truetemp\\multi-processing-demo.log"

def setup_logging(log_file: str, worker_name: str):
    """Sets up logging to both a file and stdout."""
    # Create a logger    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Clear existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(process)d - %(message)s'))
    logger.addHandler(file_handler)

    # Stream handler for stdout
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(process)d - %(message)s'))
    logger.addHandler(stream_handler)

    logging.info(f"Setting up logging , current process id is : {os.getpid()}, worker name: {worker_name}")
    return logger

def worker(name):
    setup_logging(log_file=LOG_FILE, worker_name=name)
    logging.info(f"Worker {name} started")
    print(f"Worker {name} is doing some work...")
    time.sleep(2)
    logging.info(f"Worker {name} finished")
    print(f"Worker {name} has completed its task")
    return f"Result from worker:{name}"


def start_workers():
    names = [f"Worker-{i+1}" for i in range(5)]
    with Pool(processes=3) as pool:
        results = pool.map(worker, names)
    logging.info(f"Results: {results}")
    logging.info("All workers finished")
    logging.info("---------------------------")


if __name__ == "__main__":
    setup_logging(log_file=LOG_FILE, worker_name="Main")
    logging.info("*********")
    logging.info("Main Script started")
    start_workers()
