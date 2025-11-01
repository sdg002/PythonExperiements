import logging
import numpy as np
import os
import psutil
import time
import gc
from common import log_current_process_memory_usage, log_overall_memory


def allocate_and_deallocate_memory():
    """Allocates and deallocates memory in a loop."""
    for i in range(5):
        log_current_process_memory_usage(f"Before allocation {i+1}")
        log_overall_memory()

        # Allocate a large NumPy array
        large_array = np.zeros((10000, 10000))  # Approximately 800 MB
        log_current_process_memory_usage(f"After allocation {i+1}")
        log_overall_memory()

        # Simulate some processing time
        time.sleep(2)

        # Deallocate memory by deleting the array
        del large_array

        # Force garbage collection
        gc.collect()
        log_current_process_memory_usage(f"After deallocation {i+1}")
        log_overall_memory()

def allocate_and_hold_memory(n):
    """Allocates memory in a loop and holds on to the objects."""
    held_objects = []
    for i in range(n):
        log_current_process_memory_usage(f"Before allocation {i+1}")
        log_overall_memory()
        # Allocate a large NumPy array
        large_array = np.zeros((10000, 10000))  # Approximately 800 MB
        held_objects.append(large_array)
        log_current_process_memory_usage(f"After allocation {i+1}")
        log_overall_memory()

    return held_objects

def main():
    try:
        # Configure logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Starting memory allocation and deallocation script.")
        log_current_process_memory_usage("Start")
        log_overall_memory()
        #allocate_and_deallocate_memory()
        held_objects = allocate_and_hold_memory(10)
        logging.info("Holding allocated memory for a while.")
        time.sleep(2)
        logging.info("Releasing held memory.")
        del held_objects
        gc.collect()
        log_current_process_memory_usage("After releasing held memory")
        log_overall_memory()
        logging.info("Memory allocation and deallocation script completed successfully.")
    except Exception as e:
        logging.error("An error occurred: %s", e, exc_info=True)

if __name__ == "__main__":
    main()
