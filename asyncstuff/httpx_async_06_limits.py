"""
We are calling several REST endpoints asynchronously using httpx.
- Create a Task for each request
- Add each Task to a list
- Use asyncio.gather to run all Tasks concurrently
- The return value from gather is an enumerator of all responses
- Most important - We are using the limits parameter to limit the number of concurrent requests
What did we learn?
- With variable max_concurrent, we can control the number of concurrent requests
- If max_concurrent is 1, it behaves like a synchronous call
- 1, 20,19,20
- 2, 10.3,10,9.7
- 5, 5,4.9,4.6
- 10,2.95,3.27,3.09
- 20,1.76,2.08,1.67
- 25,1.66,1.68,1.64

"""
import sys
import asyncio
import time
import httpx

URL = "http://localhost:5000/random-number"  # Change to your REST endpoint
N = 25  # Total number of calls


async def fetch_with_semaphore(client, url, idx):    
    response = await client.get(url)
    data = response.json()
    print(f"Call {idx+1}: {data}")
    return data

async def main():
    start = time.time()
    max_concurrent=int(sys.argv[1])
    print(f"Max concurrent requests: {max_concurrent}")
    timeout = httpx.Timeout(None) #5.0, pool=2.0
    limits = httpx.Limits(max_connections=max_concurrent, max_keepalive_connections=max_concurrent,keepalive_expiry=30)
    async with httpx.AsyncClient(limits=limits, timeout=timeout) as client:
        tasks = [
        fetch_with_semaphore(client, URL, i)
            for i in range(N)
        ]
        results=await asyncio.gather(*tasks,return_exceptions=True)
    elapsed = time.time() - start
    print(f"Total time elapsed: {elapsed:.2f} seconds")
    print(f"Results: {results}")


if __name__ == "__main__":
    asyncio.run(main())
