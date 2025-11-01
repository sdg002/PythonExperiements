import multiprocessing
import os

def worker_function(name):
    """Worker function to demonstrate multiprocessing."""
    return f"Process ID: {os.getpid()}, Name: {name}, Env Var from parent: {os.environ.get('DEMO_VARIABLE')}"

def main():
    os.environ['DEMO_VARIABLE'] = f'DemoValue-{os.getpid()}'
    print(f"Main Process ID: {os.getpid()}")

    # Create a pool of workers
    with multiprocessing.Pool(processes=4) as pool:
        worker_names = [f"Worker-{i+1}" for i in range(10)]
        results = pool.map(worker_function, worker_names)

    # Print results from each worker
    print("Results from workers:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
