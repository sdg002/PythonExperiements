"""
We are calling several REST endpoints asynchronously using httpx.
- Use the tenacity retry decorator
- If the random number is divisible by 7, we simulate a failure
- Do some logging
What did we learn?
WARNING:__main__:Starting call to '__main__.call_http_endpoint', this is the 1st time calling it.

Why tenacity?
https://www.python-httpx.org/advanced/transports/ (see recommendation)

Where can I find examples with tenacity?
https://github.com/jd/tenacity#before-and-after-retry-and-logging


"""
import asyncio
import logging
import time
import httpx
import tenacity as tn

URL = "http://localhost:5000/random-number"
N = 25  # Number of calls


@tn.retry(
        stop=tn.stop_after_attempt(5),
        wait=tn.wait_exponential(multiplier=1, min=4, max=10),
        after=tn.after_log(logging.getLogger(__name__), logging.WARNING))
async def call_http_endpoint(client: httpx.AsyncClient)->httpx.Response:
    #YOU WERE HERE
    url=f"{URL}"
    response = await client.get(url)
    response.raise_for_status()
    data = response.json()
    random_number=data["number"]
    logging.info(f"Response from {url}: {random_number}")
    # Simulate a failure below
    if random_number%2 ==0:
        logging.error(f"Simulating failure for {random_number}")
        raise Exception
    return random_number

async def main():
    no_of_attempts = list(range(N))
    start = time.time()
    async with httpx.AsyncClient() as client:
        tasks=[]
        for number in no_of_attempts:
            logging.info(f"Going to prepare Task for {number}")
            tasks.append(call_http_endpoint(client))
        logging.info(f"Prepared {len(tasks)} Tasks, going to run them concurrently")
        responses = await asyncio.gather(*tasks)
        logging.info("Wait complete..going to enumerate responses")
        for i, response in enumerate(responses):
            random_number = response            
            logging.info(f"Call {i+1}: {random_number=}")
    elapsed = time.time() - start
    logging.info(f"Total time elapsed: {elapsed:.2f} seconds")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
