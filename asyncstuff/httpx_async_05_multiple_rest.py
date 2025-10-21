"""
We are 
- We are calling an asynchronous function which in turn calls 2 REST endpoints sequentially and asynchronously
- This function is called multiple times concurrently
What do we learn?
- The N+1 call to REST end point is initiated before the N call is completed
- The overall time is 2.15 seconds
"""
import asyncio
import time
import httpx

N = 5  # Number of calls
URL_SQUARE = "http://localhost:5000/square"
URL_RANDOM = "http://localhost:5000/random-number" 

async def async_call_multiple_rest_end_points(seconds:float, index:int):
    print(f"BEGIN-Going to call 2 REST endpoints asynchronously with index {index} ")
    async with httpx.AsyncClient() as client:
        # First call
        url = f"{URL_SQUARE}/{index}"
        print(f"{index=}-First-Calling REST endpoint: {url}")
        first_response = await client.get(url)
        data = first_response.json()
        print(f"{index=}-First-Response from first:{url}: {data}")
        # Second call
        print(f"{index=}-Second-Calling REST endpoint: {URL_RANDOM}")
        second_response = await client.get(URL_RANDOM)
        data = second_response.json()
        print(f"{index=}-Second-Response from second:{URL_RANDOM}: {data}")
    print(f"COMPLETE-Function called with index {index}!")
    return f"Result from async function with 2 REST calls,index {index}"

async def main():
    start = time.time()
    tasks=[]
    for index in list(range(N)):
        tasks.append(async_call_multiple_rest_end_points(seconds=2, index=index))
    print(f"Prepared {len(tasks)} Tasks, going to run them concurrently")
    responses = await asyncio.gather(*tasks)      
    print("Wait complete..going to enumerate responses")
    for i, response in enumerate(responses):
        print(f"Call {i}: {response=}")
    elapsed = time.time() - start
    print(f"Total time elapsed: {elapsed:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
