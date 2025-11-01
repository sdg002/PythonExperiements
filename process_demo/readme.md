[[_TOC_]]

# About
Simple experiments with launching processes from Python
- Popen
- Redirect standard output and standard error to a file
- Launch a PowerShell script from Python

---

# Multi-processing demo with logging

## Which file?
See this [file](multi_processing_with_logging.py)

## What did we do here?
- Spawn multiple process with a limited process pool
- Collect the results from each of the worker jobs
- Initialize logging every time

## What are the issues with logging ?
The child function does not have context of the parent process and hence logging has to be initialized once again
But, we have to remember that the processes are not terminated, i.e the same process will be re-used for subsequent worker function invocation

---

# Multi-processing demo with environment variable inheritance
See this [file](multi_processing_environment_variabes.py)
The child processes will inherit the variable set in the parent. This was expected

# Multi-processing demo with Pandas dataframe
See this [file](multi_processing_with_pandas.py)
The child processes are generating a Pandas dataframe. The frames are joined into a single large frame in the caller process
