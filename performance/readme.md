[[_TOC_]]

# What am I doing ?
Trying to find out how to log the memory consumption by a process

---

# How to measure memory?
RSS (Resident Set Size) and VMS (Virtual Memory Size) are metrics used to measure memory usage by a process:

1. ## RSS (Resident Set Size)
   - Represents the portion of memory occupied by a process that is held in RAM.
   - It includes memory allocated for the process's code, data, and stack, as well as memory mapped files.
   - RSS does not include memory that has been swapped out to disk.

2. ## VMS (Virtual Memory Size)
   - Represents the total amount of virtual memory allocated for a process.
   - It includes all memory the process can access, including memory that is not currently in RAM (e.g., swapped out or memory-mapped files).
   - VMS is typically larger than RSS because it includes memory that may not be actively used.

In simpler terms:
- RSS is the actual memory in use in RAM.
- VMS is the total memory reserved for the process, including memory that may not be actively used.
- 

---

# How to log the memory usage ?

See function `log_memory_usage` in the file [common.py](common.py)

```python
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    logging.info(f"Stage {stage[:30].ljust(30)} | RSS: {memory_info.rss / (1024 * 1024):>10.2f} MB | VMS: {memory_info.vms / (1024 * 1024):>10.2f} MB")
```

---

# How to release memory?
See the this [runner file](main_alloc_and_release.py).

```python
    # Deallocate memory by deleting the array
    del large_array
    
    # Force garbage collection
    gc.collect()
```
