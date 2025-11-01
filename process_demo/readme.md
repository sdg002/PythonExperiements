[[_TOC_]]

# About
Simple experiments with launching processes from Python
- Popen
- Redirect standard output and standard error to a file
- Launch a PowerShell script from Python

---

# Multi-processing demo

## Which file?
See this [file](multi-processing.py)

## What did we do here?
- Spawn multiple process with a limited process pool
- Collect the results from each of the worker jobs
- Initialize logging every time

## What are the issues with logging ?
The child function does not have context of the parent process and hence logging has to be initialized once again
But, we have to remember that the processes are not terminated, i.e the same process will be re-used for subsequent worker function invocation

---
