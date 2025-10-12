from typing import Optional
import asyncio
import logging
import pandas as pd
import httpx

class WeatherScraper:
    def __init__(self, base_url, mock_transport: Optional[httpx.MockTransport]=None):
        self.base_url = base_url
        self.__mock_transport=mock_transport
        logging.info(f"WeatherScraper initialized with base URL: {self.base_url}")

    def create_httpx_client(self)->httpx.AsyncClient:
        """
        Create an httpx client with custom transport
        """
        logging.info("Going to create an instance of AsyncClient")
        if self.__mock_transport is None:
            logging.info("ctor-Using live transport")
            return httpx.AsyncClient()
        else:
            logging.info("ctor-Using mock transport")
            return httpx.AsyncClient(transport=self.__mock_transport)        

    async def get_weather_async(self):
        async with self.create_httpx_client() as client:
            url = f"{self.base_url}"
            logging.info(f"Fetching weather data from {url}")
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame(data)
            logging.info(f"Weather data retrieved successfully: {len(df)} records")
            return df

async def main():
    scraper = WeatherScraper("http://localhost:5000/weather")
    df = await scraper.get_weather_async()
    print(df)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())