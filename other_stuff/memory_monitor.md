[[_TOC_]]

# What am I doing ?
Trying to find out how to log the memory consumption by a process

# Understanding
RSS (Resident Set Size) and VMS (Virtual Memory Size) are metrics used to measure memory usage by a process:

1. **RSS (Resident Set Size)**:
   - Represents the portion of memory occupied by a process that is held in RAM.
   - It includes memory allocated for the process's code, data, and stack, as well as memory mapped files.
   - RSS does not include memory that has been swapped out to disk.

2. **VMS (Virtual Memory Size)**:
   - Represents the total amount of virtual memory allocated for a process.
   - It includes all memory the process can access, including memory that is not currently in RAM (e.g., swapped out or memory-mapped files).
   - VMS is typically larger than RSS because it includes memory that may not be actively used.

In simpler terms:
- RSS is the actual memory in use in RAM.
- VMS is the total memory reserved for the process, including memory that may not be actively used.