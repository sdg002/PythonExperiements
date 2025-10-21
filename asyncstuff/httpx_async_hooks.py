"""
We are calling several REST endpoints asynchronously using httpx.
- Create a Task for each request
- Add each Task to a list
- Use asyncio.gather to run all Tasks concurrently
- The return value from gather is an enumerator of all responses
- Most important - We are interecepting the response using a hook

"""
import httpx
import asyncio
import time

URL = "http://localhost:5000/random-number"  # Change to your REST endpoint
N = 20  # Number of calls

async def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code} - content-length:{response.headers['Content-Length']}")

async def main():
    start = time.time()
    async with httpx.AsyncClient(event_hooks={"response": [log_response]}) as client:
        tasks = [client.get(URL) for _ in range(N)]
        print("Before-gather")
        responses = await asyncio.gather(*tasks)
        print("After-gather")
        for i, response in enumerate(responses):
            data = response.json()
            print(f"Call {i+1}: {data}")
    elapsed = time.time() - start
    print(f"Total time elapsed: {elapsed:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
