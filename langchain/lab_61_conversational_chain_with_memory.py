"""
A conversational chain with memory to remember previous interactions.
In this example:
1. Load environment variables using dotenv.
2. Initialize a ChatOpenAI model.
3. Set up a ConversationBufferMemory to store the conversation history.
4. Create a ConversationChain that uses the LLM and memory.
5. Invoke the chain with user inputs and see how it remembers past interactions.
6. Print the responses to observe the conversation flow. (verbose mode is enabled to show steps.)

When you run this script, you will see that there is a `history` key in the memory
that keeps track of the conversation. The `input` to the chain is the latest user message
"""

import dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain


if __name__ == "__main__":
    dotenv.load_dotenv(override=True)
    llm = ChatOpenAI(model="gpt-4o-mini")

    memory = ConversationBufferMemory(return_messages=True)

    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True,  # prints steps; useful while learning
    )

    print(conversation.invoke("Hi, my name is Saurabh."))
    print("----------------------")
    print(conversation.invoke("What did I just tell you my name is?"))
    print("----------------------")
    print(conversation.invoke("Suggest a fun weekend activity near London, UK."))
    print("----------------------")
