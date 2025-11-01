import logging
import numpy as np
import os
import psutil
import time
import gc
from common import log_memory_usage


def allocate_and_deallocate_memory():
    """Allocates and deallocates memory in a loop."""
    for i in range(5):
        log_memory_usage(f"Before allocation {i+1}")

        # Allocate a large NumPy array
        large_array = np.zeros((10000, 10000))  # Approximately 800 MB
        log_memory_usage(f"After allocation {i+1}")

        # Simulate some processing time
        time.sleep(2)

        # Deallocate memory by deleting the array
        del large_array

        # Force garbage collection
        gc.collect()
        log_memory_usage(f"After deallocation {i+1}")

def allocate_and_hold_memory(n):
    """Allocates memory in a loop and holds on to the objects."""
    held_objects = []
    for i in range(n):
        log_memory_usage(f"Before allocation {i+1}")

        # Allocate a large NumPy array
        large_array = np.zeros((10000, 10000))  # Approximately 800 MB
        held_objects.append(large_array)
        log_memory_usage(f"After allocation {i+1}")

    return held_objects

def main():
    try:
        # Configure logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Starting memory allocation and deallocation script.")
        #allocate_and_deallocate_memory()
        held_objects = allocate_and_hold_memory(10)
        logging.info("Holding allocated memory for a while.")
        time.sleep(2)
        logging.info("Releasing held memory.")
        del held_objects
        gc.collect()
        log_memory_usage("After releasing held memory")
        logging.info("Memory allocation and deallocation script completed successfully.")
    except Exception as e:
        logging.error("An error occurred: %s", e, exc_info=True)

if __name__ == "__main__":
    main()
