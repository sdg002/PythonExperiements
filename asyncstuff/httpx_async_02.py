"""
We are calling several REST endpoints asynchronously using httpx.
- Create a Task for each request
- Pass some payload to each request (we did not do this in 01)
- Add each Task to a list
- Use asyncio.gather to run all Tasks concurrently
- The return value from gather is an enumerator of all responses

"""
import asyncio
import time
import httpx

URL = "http://localhost:5000/square"  # Change to your REST endpoint
N = 5  # Number of calls

async def main():
    numbers_to_square = list(range(N))
    start = time.time()
    async with httpx.AsyncClient() as client:
        tasks=[]
        for number in numbers_to_square:
            url=f"{URL}/{number}"
            print(f"Going to prepare Task for {url}")
            tasks.append(client.get(url))
        print(f"Prepared {len(tasks)} Tasks, going to run them concurrently")
        responses = await asyncio.gather(*tasks)
        print("Wait complete..going to enumerate responses")
        for i, response in enumerate(responses):
            data = response.json()
            print(f"Call {i+1}: {data}")
    elapsed = time.time() - start
    print(f"Total time elapsed: {elapsed:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
