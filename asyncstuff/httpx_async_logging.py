"""
We are calling several REST endpoints asynchronously using httpx.
- Create a Task for each request
- Add each Task to a list
- Use asyncio.gather to run all Tasks concurrently
- The return value from gather is an enumerator of all responses
- Most important - use logging
What did we learn?
With level set to INFO
INFO [2025-07-24 17:54:30,537] httpx - HTTP Request: GET http://localhost:5000/random-number "HTTP/1.1 200 OK"


With level set to DEBUG
For every request we get the following output:
DEBUG [2025-07-24 18:00:09,459] httpcore.http11 - receive_response_body.started request=<Request [b'GET']>
DEBUG [2025-07-24 18:00:09,463] httpcore.http11 - response_closed.complete
DEBUG [2025-07-24 18:00:09,469] httpcore.http11 - receive_response_body.complete
DEBUG [2025-07-24 18:00:09,470] httpcore.http11 - response_closed.started
DEBUG [2025-07-24 18:00:09,473] httpcore.http11 - receive_response_body.complete
DEBUG [2025-07-24 18:00:09,475] httpcore.http11 - response_closed.started
DEBUG [2025-07-24 18:00:09,477] httpcore.http11 - response_closed.complete
DEBUG [2025-07-24 18:00:09,479] httpcore.http11 - response_closed.complete

Challenging
"""
import logging
import httpx
import asyncio
import time

URL = "http://localhost:5000/random-number"  # Change to your REST endpoint
N = 20  # Number of calls

async def main():
    start = time.time()
    async with httpx.AsyncClient() as client:
        tasks = [client.get(URL) for _ in range(N)]
        responses = await asyncio.gather(*tasks)
        for i, response in enumerate(responses):
            data = response.json()
            logging.info(f"Call {i+1}: {data}")
    elapsed = time.time() - start
    logging.info(f"Total time elapsed: {elapsed:.2f} seconds")


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",level=logging.DEBUG)
    logging.getLogger("httpx").setLevel(logging.DEBUG)
    asyncio.run(main())
