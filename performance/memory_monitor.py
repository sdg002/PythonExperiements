import logging
import numpy as np
from lib import log_memory_usage

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def allocate_memory():
    """Allocates memory in stages and logs memory usage."""
    log_memory_usage("Start")

    # Stage 1: Allocate a large list
    large_list = [0] * 10**7  # Approximately 80 MB
    log_memory_usage("After allocating large list")

    # Stage 2: Allocate a large NumPy array
    large_array = np.zeros((1000, 1000))  # Approximately 8 MB
    log_memory_usage("After allocating large NumPy array")

    # Stage 3: Allocate another large list
    another_large_list = [1] * 10**7  # Approximately 80 MB
    log_memory_usage("After allocating another large list")

    # Stage 4: Allocate a large dictionary
    large_dict = {i: i for i in range(10**6)}  # Approximately 32 MB
    log_memory_usage("After allocating large dictionary")

    # Stage 5: Allocate a large dictionary
    large_dict_5 = {i: i for i in range(10**6)}  # Approximately 32 MB
    log_memory_usage("After allocating large dictionary")

    # Stage 6: Allocate a large dictionary
    large_dict_6 = {i: i for i in range(10**6)}  # Approximately 32 MB
    log_memory_usage("After allocating large dictionary")

    # Prevent variables from being garbage collected immediately
    return large_list, large_array, another_large_list, large_dict, large_dict_5, large_dict_6

def main():
    try:
        logging.info("Starting memory allocation script.")
        allocate_memory()
        logging.info("Memory allocation script completed successfully.")
    except Exception as e:
        logging.error("An error occurred: %s", e, exc_info=True)

if __name__ == "__main__":
    main()
