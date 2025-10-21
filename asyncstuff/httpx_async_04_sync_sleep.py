"""
We are 
- We are calling a function which sleeps synchronously (not async sleep)
- This function is called multiple times concurrently
What do we learn?
- This is a synchronous function, so it blocks the event loop
- The total time taken will be the sum of all sleep durations
- The total time is > 10 seconds. Compare with 03.py which takes about 2 seconds

"""
import time
import asyncio

N = 5  # Number of calls

async def async_sleep_demo(seconds:float, index:int):
    print(f"Sleeping asynchronously for {seconds} seconds...")
    time.sleep(seconds)
    print(f"Function called with index {index}!")
    return f"Result from async_sleep_demo with index {index}"

async def main():
    start = time.time()
    tasks=[]
    for index in list(range(N)):
        tasks.append(async_sleep_demo(seconds=2, index=index))  # Example of a task to sleep for 2 seconds
    print(f"Prepared {len(tasks)} Tasks, going to run them concurrently")
    responses = await asyncio.gather(*tasks)      
    print("Wait complete..going to enumerate responses")
    for i, response in enumerate(responses):
        print(f"Call {i}: {response=}")
    elapsed = time.time() - start
    print(f"Total time elapsed: {elapsed:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
