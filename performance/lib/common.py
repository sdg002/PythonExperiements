import logging
import os
import psutil

def log_memory_usage(stage: str):
    """Logs the current memory usage."""
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    logging.info(f"Stage {stage[:30].ljust(30)} | RSS: {memory_info.rss / (1024 * 1024):>10.2f} MB | VMS: {memory_info.vms / (1024 * 1024):>10.2f} MB")
