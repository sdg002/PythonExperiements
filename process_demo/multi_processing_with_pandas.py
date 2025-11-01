import multiprocessing
import pandas as pd
import numpy as np
import os

def generate_random_dataframe(worker_id):
    """Worker function to generate a randomized Pandas DataFrame."""
    print(f"Worker {worker_id} running in process ID: {os.getpid()}")
    row_count = 10
    data = {
        'A': np.random.randint(0, 100, row_count),
        'B': np.random.rand(row_count),
        'Worker': [worker_id] * row_count,
        'Timestamp': pd.date_range(start='2025-01-01', periods=row_count, freq='s')
    }
    return pd.DataFrame(data)

def main():
    print(f"Main Process ID: {os.getpid()}")

    # Create a pool of workers
    with multiprocessing.Pool(processes=4) as pool:
        worker_ids = [f"Worker-{i+1}" for i in range(4)]
        dataframes = pool.map(generate_random_dataframe, worker_ids)

    # Combine all DataFrames into one
    combined_dataframe = pd.concat(dataframes, ignore_index=True)
    print("Combined DataFrame:")
    print(combined_dataframe)

if __name__ == "__main__":
    main()
