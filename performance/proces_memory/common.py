import logging
import os
import psutil

def log_current_process_memory_usage(stage: str):
    """Logs the current memory usage."""
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    stage=f"Stage {stage}"
    logging.info(f"{stage[:30].ljust(30)} | RSS: {memory_info.rss / (1024 * 1024):>10.2f} MB | VMS: {memory_info.vms / (1024 * 1024):>10.2f} MB")

def log_overall_memory():
    """Logs the current overall memory usage."""
    memory = psutil.virtual_memory()
    process = psutil.Process()
    total_memory = f"Total Memory: {memory.total / (1024 * 1024):.2f} MB"
    #logging.info(f"{total_memory[:30].ljust(30)} | Used: {memory.used / (1024 * 1024):.2f} MB | Available: {memory.available / (1024 * 1024):.2f} MB | Percent Used: {memory.percent}% | {process.memory_info().rss/(1024*1024):.2f} MB RSS | {memory.percent}% | {process.memory_info().vms/(1024*1024):.2f} MB VMS")
    logging.info(f"{memory}| {memory.used / (1024 * 1024):.2f} MB Used")
    #logging.info(f"Total | {memory.used / (1024 * 1024):.2f} MB")