from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import dotenv


if __name__ == "__main__":
    dotenv.load_dotenv(override=True)
    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = ChatPromptTemplate.from_template(
        "You are a helpful assistant. Summarize the following text in 2 sentences:\n\n{text}"
    )

    messages = prompt.format_messages(
        text="LangChain is a Python framework for building applications with LLMs."
    )

    response = llm.invoke(messages)
    print(response.content)
