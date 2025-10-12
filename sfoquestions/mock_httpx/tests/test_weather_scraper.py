import logging
import asyncio
import pandas as pd
import pytest
import httpx
from stackoverflow.mock_httpx.src.weather_scraper import WeatherScraper


def test_ctor():
    # Arrange
    scraper = WeatherScraper(base_url="http://example.com")

    # Assert
    assert scraper.base_url == "http://example.com"

@pytest.mark.asyncio
async def test_when_method_get_weather_then_dataframe_must_be_returned():
    # Arrange
    mock_records= [{"city": "city001", "temperature": 21},
              {"city": "city002", "temperature": 22}]

    def mock_handler(request: httpx.Request) ->httpx.Response:
        logging.info(f"mock-handler:-Goint to handle {request.method} {request.url}")
        return httpx.Response(200, json=mock_records)

    mock_transport = httpx.MockTransport(handler=mock_handler)
    scraper = WeatherScraper(base_url="http://some.mocksite.com/weather", mock_transport=mock_transport)

    # Act
    df_actual = await scraper.get_weather_async()

    # Assert
    assert isinstance(df_actual, pd.DataFrame)
    assert len(df_actual) == len(mock_records)
    assert set(df_actual.columns) == {"city", "temperature"}
    assert df_actual["city"].tolist() == [record["city"] for record in mock_records]
    assert df_actual["temperature"].tolist() == [record["temperature"] for record in mock_records]
    logging.info(f"DataFrame:\n{df_actual.to_string(index=False)}")