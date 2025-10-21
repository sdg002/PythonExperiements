"""
We are calling several REST endpoints asynchronously using httpx.
- We are not calling the actual web service but a mock method

"""
import logging
import httpx
import asyncio
import time

URL = "http://localhost:5000/random-number"  # Change to your REST endpoint
N = 5  # Number of calls

def handler(request: httpx.Request) ->httpx.Response:
    logging.info(f"Mock-Inside {request.method} {request.url}")
    return httpx.Response(200, json={"text": "Hello, world from mock handler!"})

async def main():
    start = time.time()
    mock_transport = httpx.MockTransport(handler=handler)
    async with httpx.AsyncClient(transport=mock_transport) as client:
        tasks = [client.get(URL) for _ in range(N)]
        responses = await asyncio.gather(*tasks)
        for i, response in enumerate(responses):
            data = response.json()
            print(f"Call {i+1}: {data}")
    elapsed = time.time() - start
    print(f"Total time elapsed: {elapsed:.2f} seconds")


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s [%(asctime)s] %(name)s - %(message)s", level=logging.INFO)
    asyncio.run(main())
