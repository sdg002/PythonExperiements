import dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


if __name__ == "__main__":
    dotenv.load_dotenv(override=True)
    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = ChatPromptTemplate.from_template(
        "Translate the following sentence to {language}:\n\n{sentence}"
    )

    # Chain = prompt then model
    chain = prompt | llm

    result = chain.invoke(
        {"language": "French", "sentence": "I love building with LangChain."})
    print(result.content)
