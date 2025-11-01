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

def main():
    try:
        # Configure logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Starting memory allocation and deallocation script.")
        allocate_and_deallocate_memory()
        logging.info("Memory allocation and deallocation script completed successfully.")
    except Exception as e:
        logging.error("An error occurred: %s", e, exc_info=True)

if __name__ == "__main__":
    main()
