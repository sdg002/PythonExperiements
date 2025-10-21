"""
We are 
- We are calling a function which sleeps asynchronously
- This function is called multiple times concurrently
What do we learn?
- This is an asynchronous function, so it does not block the event loop
- The total time taken will be the maximum sleep duration, not the sum
- The thread id was same for all calls, indicating they were run in the same event loop

"""
import asyncio
import time
import threading

N = 5  # Number of calls

async def async_sleep_demo(seconds:float, index:int):
    print(f"{index}-Sleeping asynchronously for {seconds} seconds...{threading.get_ident()}")
    await asyncio.sleep(seconds)
    print(f"Function called with index {index}!")
    return f"{index}-Result from async_sleep_demo with index {index}"

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
