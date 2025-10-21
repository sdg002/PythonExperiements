"""
We are calling several REST endpoints asynchronously using httpx.
- Create a Task for each request
- Add each Task to a list
- Use asyncio.gather to run all Tasks concurrently
- The return value from gather is an enumerator of all responses
- Most important - We are using a semaphone to limit the number of concurrent requests
What did we learn?
- With variable max_concurrent, we can control the number of concurrent requests
- If max_concurrent is 1, it behaves like a synchronous call
- max_concurrent vs total time
- 1, 21
- 2, 11,10.91
- 5, 5.19,5.53
- 10,3.24,3.56,3.11
- 20,3.46,2.38,2.92
- 25,1.67,1.92,2.10

"""
import sys
import httpx
import asyncio
import time

URL = "http://localhost:5000/random-number"  # Change to your REST endpoint
N = 25  # Total number of calls


async def fetch_with_semaphore(client, url, sem, idx):
    async with sem:
        response = await client.get(url)
        data = response.json()
        print(f"Call {idx+1}: {data}")
        return data

async def main():
    start = time.time()
    max_concurrent=int(sys.argv[1])
    sem = asyncio.Semaphore(max_concurrent)
    async with httpx.AsyncClient() as client:
        tasks = [
            fetch_with_semaphore(client, URL, sem, i)
            for i in range(N)
        ]
        await asyncio.gather(*tasks)
    elapsed = time.time() - start
    print(f"Total time elapsed: {elapsed:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
