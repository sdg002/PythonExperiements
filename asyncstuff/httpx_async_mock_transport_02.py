"""
https://stackoverflow.com/questions/70633584/how-to-mock-httpx-asyncclient-in-pytest
"""
import logging
import asyncio
import time
from typing import Optional
import httpx


class MyScraper():
    URL = "http://localhost:5000/random-number"  # Change to your REST endpoint
    def __init__(self, mock_transport: Optional[httpx.MockTransport] ):
        self.__mock_transport=mock_transport
        pass

    def create_httpx_client(self)->httpx.AsyncClient:
        """
        Create an httpx client with custom transport, limits, and timeout.
        """
        print("Going to create an instance of AsyncClient")
        if self.__mock_transport is None:
            print("ctor-Using live transport")
            return httpx.AsyncClient()
        else:
            print("ctor-Using mock transport")
            return httpx.AsyncClient(transport=self.__mock_transport)
        #httpx.AsyncClient(transport=mock_transport) 

    async def fetch_random_number(self)->int:
        #async with httpx.AsyncClient() as client:
        async with self.create_httpx_client() as client:
            response=await client.get(self.URL)
            data = response.json()
            random_number = data["number"]
            return random_number
        pass
################


def handler(request: httpx.Request) ->httpx.Response:
    print(f"mock-inside {request.method} {request.url}")
    fake_payload={"number": 1234}
    return httpx.Response(200, json=fake_payload)

async def main():
    scraper_live=MyScraper(mock_transport=None)
    result=await scraper_live.fetch_random_number()
    print(f"Random number fetched using live: {result}")
    print("----------------------")
    mock_transport = httpx.MockTransport(handler=handler)
    scraper_mock=MyScraper(mock_transport=mock_transport)
    result=await scraper_mock.fetch_random_number()
    print(f"Random number fetched using mock: {result}")


    # start = time.time()
    # mock_transport = httpx.MockTransport(handler=handler)
    # async with httpx.AsyncClient(transport=mock_transport) as client:
    #     tasks = [client.get(URL) for _ in range(N)]
    #     responses = await asyncio.gather(*tasks)
    #     for i, response in enumerate(responses):
    #         data = response.json()
    #         print(f"Call {i+1}: {data}")
    # elapsed = time.time() - start
    # print(f"Total time elapsed: {elapsed:.2f} seconds")


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s [%(asctime)s] %(name)s - %(message)s", level=logging.INFO)
    asyncio.run(main())
