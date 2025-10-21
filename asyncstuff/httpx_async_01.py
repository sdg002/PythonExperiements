"""
We are calling several REST endpoints asynchronously using httpx.
- Create a Task for each request
- Add each Task to a list
- Use asyncio.gather to run all Tasks concurrently
- The return value from gather is an enumerator of all responses

"""
import httpx
import asyncio
import time

URL = "http://localhost:5000/random-number"  # Change to your REST endpoint
N = 5  # Number of calls

async def main():
    start = time.time()
    async with httpx.AsyncClient() as client:
        tasks = [client.get(URL) for _ in range(N)]
        responses = await asyncio.gather(*tasks)
        for i, response in enumerate(responses):
            data = response.json()
            print(f"Call {i+1}: {data}")
    elapsed = time.time() - start
    print(f"Total time elapsed: {elapsed:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
