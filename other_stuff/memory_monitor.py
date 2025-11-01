import logging
import os
import psutil
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_memory_usage(stage):
    """Logs the current memory usage."""
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    logging.info(f"Stage {stage}: RSS = {memory_info.rss / (1024 * 1024):.2f} MB, VMS = {memory_info.vms / (1024 * 1024):.2f} MB")

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

    # Prevent variables from being garbage collected immediately
    return large_list, large_array, another_large_list, large_dict

def main():
    try:
        logging.info("Starting memory allocation script.")
        allocate_memory()
        logging.info("Memory allocation script completed successfully.")
    except Exception as e:
        logging.error("An error occurred: %s", e, exc_info=True)

if __name__ == "__main__":
    main()
