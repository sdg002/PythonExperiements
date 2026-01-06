import os
from langchain_openai import ChatOpenAI
import dotenv


if __name__ == "__main__":
    dotenv.load_dotenv(override=True)
    print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")
    llm = ChatOpenAI(model="gpt-5-nano")  # or another model name

    response = llm.invoke("Say hello in one sentence.")
    print(response.content)
