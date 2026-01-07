"""
An example of using Structured Output Parser with ChatOpenAI.
In this example we define a structure for the output we want from the model,
generate a prompt with format instructions, and parse the output into a structured format.
1. Define the desired output structure using ResponseSchema.
2. Create a StructuredOutputParser from the schemas.
3. Generate format instructions from the parser.
4. Create a prompt template that includes the format instructions.
5. Use ChatOpenAI to generate a response based on the prompt.
6. The raw output from the model is in markdown format.
7. Parse the model's raw output using the StructuredOutputParser.(using the `parse` method)

The response from the model is split into  `title` and `tags` fields based on the defined structure.


"""
import dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


if __name__ == "__main__":
    dotenv.load_dotenv(override=True)
    # Define the structure you want
    schemas = [
        ResponseSchema(name="title", description="A short title for the idea"),
        ResponseSchema(name="tags", description="A list of short tags"),
    ]

    parser = StructuredOutputParser.from_response_schemas(schemas)
    format_instructions = parser.get_format_instructions()

    print(f"Format Instructions:\n{format_instructions}\n")
    prompt = ChatPromptTemplate.from_template(
        "Generate a startup idea about {topic}.\n"
        "Follow these instructions when formatting the output:\n"
        "{format_instructions}"
    )
    print(f"Prompt Template:\n{prompt}\n")
    llm = ChatOpenAI(model="gpt-4o-mini")

    chain = prompt | llm

    raw = chain.invoke(
        {"topic": "personal finance apps", "format_instructions": format_instructions}
    )
    print("Raw output:\n", raw.content)

    parsed = parser.parse(raw.content)
    print("\nParsed output as dict:\n", parsed)
