"""
A Pydantic settings model that reads configuration from environment variables.
This example demonstrates how to use Pydantic's BaseSettings to manage application settings.

https://docs.pydantic.dev/latest/concepts/pydantic_settings/#environment-variable-names
"""
import os
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    app_name: str = "MyApp"
    debug: bool = False
    database_url: str

    class Config:
        env_prefix = "MYAPP_"


# Set an environment variable for demo
os.environ["MYAPP_DATABASE_URL"] = "postgresql://user:pass@localhost:5432/db"
os.environ["MYAPP_DEBUG"] = "true"

settings = AppSettings()
print(settings)
print("Debug:", settings.debug)
print("Database:", settings.database_url)
