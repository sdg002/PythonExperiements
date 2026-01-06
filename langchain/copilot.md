[[_TOC_]]


## Overview
Here’s a hands-on, step-by-step LangChain guide you can follow in order. I’ll assume you know basic Python and want to build simple LLM-powered scripts.

---

## 1. What LangChain is and when to use it

LangChain is a Python framework that helps you build applications around large language models (LLMs): chatbots, summarizers, RAG systems, tool-using agents, etc., by composing pieces like models, prompt templates, memory, tools, and retrieval into “chains.”

You use LangChain when:
- **You want structure** around prompts, not just ad‑hoc API calls.
- **You need multiple steps** (e.g., prompt → parse output → call another tool).
- **You want reusable components**: prompt templates, chains, and agents.

---

## 2. Installation and basic setup

### 2.1. Install LangChain and a model provider

The exact packages depend on the LLM provider you want. The most common is OpenAI‑compatible APIs.

```bash
pip install langchain langchain-openai
```

You’ll also need an API key (e.g., from OpenAI or any compatible provider) and set it as an environment variable:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

On Windows (PowerShell):

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

### 2.2. Your first “Hello LLM” with LangChain

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")  # or another model name

response = llm.invoke("Say hello in one sentence.")
print(response.content)
```

Conceptually, LangChain wraps the raw model into a **Model object** (`ChatOpenAI`) so you can plug it into other components like prompt templates and chains.

---

## 3. Prompt templates (dynamic prompts)

Prompt templating lets you define reusable prompts with variables, then fill them in at runtime. This is one of the core ideas in LangChain.

### 3.1. Simple prompt template

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant. Summarize the following text in 2 sentences:\n\n{text}"
)

messages = prompt.format_messages(
    text="LangChain is a Python framework for building applications with LLMs."
)

response = llm.invoke(messages)
print(response.content)
```

What’s going on:

- **`ChatPromptTemplate`** lets you define a template with `{variables}`.
- **`format_messages`** creates the message structure the chat model expects (system/user messages).
- You can reuse `prompt` across your code with different `text` inputs.

---

## 4. Chains: combining model + prompt

A “chain” is a pipeline of components. The simplest chain is: **prompt → LLM → output**. LangChain makes this composable and debuggable.

### 4.1. A basic chain using the `|` operator

In newer LangChain versions, you can compose with the pipe operator:

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template(
    "Translate the following sentence to {language}:\n\n{sentence}"
)

# Chain = prompt then model
chain = prompt | llm

result = chain.invoke({"language": "French", "sentence": "I love building with LangChain."})
print(result.content)
```

Key ideas:

- **`chain = prompt | llm`** builds a simple chain.
- **`.invoke({...})`** runs the chain once with your input variables.
- You can later swap out the model or prompt without changing the rest of the code.

---

## 5. Parsing and structuring model output

Often you want the model’s output as structured data (e.g., JSON) instead of free text. LangChain provides **output parsers** and templates to enforce structure.

### 5.1. Use an output parser to get a Python object

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# Define the structure you want
schemas = [
    ResponseSchema(name="title", description="A short title for the idea"),
    ResponseSchema(name="tags", description="A list of short tags"),
]

parser = StructuredOutputParser.from_response_schemas(schemas)
format_instructions = parser.get_format_instructions()

prompt = ChatPromptTemplate.from_template(
    "Generate a startup idea about {topic}.\n"
    "Follow these instructions when formatting the output:\n"
    "{format_instructions}"
)

llm = ChatOpenAI(model="gpt-4o-mini")

chain = prompt | llm

raw = chain.invoke(
    {"topic": "personal finance apps", "format_instructions": format_instructions}
)
print("Raw output:\n", raw.content)

parsed = parser.parse(raw.content)
print("\nParsed output as dict:\n", parsed)
```

Here:

- **Response schemas** describe the structured fields.
- **`get_format_instructions()`** gives text you include in the prompt so the model returns structured output.
- **`parser.parse()`** converts the raw text response into a Python dict safely.

---

## 6. Memory: keeping conversation context

Memory lets your chain remember earlier messages (like a chat history) so conversations feel continuous.

### 6.1. Simple conversational chain with memory

```python
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

llm = ChatOpenAI(model="gpt-4o-mini")

memory = ConversationBufferMemory(return_messages=True)

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True,  # prints steps; useful while learning
)

print(conversation.invoke("Hi, my name is Saurabh."))
print(conversation.invoke("What did I just tell you my name is?"))
print(conversation.invoke("Suggest a fun weekend activity near Reading, UK."))
```

What to notice:

- **`ConversationBufferMemory`** stores previous messages in memory.
- Each call to `conversation.invoke(...)` sends both the new input and the history to the LLM.
- `verbose=True` helps you see what’s passed under the hood, useful as you debug chains.

---

## 7. Retrieval and basic RAG (high-level intro)

One of LangChain’s most powerful use cases is RAG (Retrieval-Augmented Generation): indexing your own data (PDFs, docs, DB) and letting the LLM answer questions using that data.

A full RAG stack involves:

1. **Load documents** (from text, PDFs, etc.).
2. **Split into chunks** (e.g., sections).
3. **Embed** each chunk into a vector representation.
4. **Store** embeddings in a vector store (e.g., FAISS, Chroma).
5. **Retrieve** top relevant chunks for a query.
6. **Combine** the retrieved context with a prompt and call the LLM.

Below is a very minimal, conceptual example using an in-memory vector store:

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate

# 1. Your documents (in practice, load from files/DB)
raw_text = """
LangChain is a framework for developing applications powered by language models. 
It enables composition of components like prompt templates, chains, and agents.
"""

# 2. Split text into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=0)
docs = splitter.create_documents([raw_text])

# 3. Create embeddings and vector store
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(docs, embeddings)

# 4. Retrieve relevant chunks
query = "What does LangChain help developers do?"
retriever = vector_store.as_retriever(k=3)
relevant_docs = retriever.invoke(query)

context = "\n\n".join(doc.page_content for doc in relevant_docs)

# 5. Build prompt with retrieved context
prompt = ChatPromptTemplate.from_template(
    "You are an expert assistant.\n\n"
    "Use the context below to answer the question.\n"
    "If the answer is not in the context, say you don't know.\n\n"
    "Context:\n{context}\n\n"
    "Question: {question}"
)

llm = ChatOpenAI(model="gpt-4o-mini")

chain = prompt | llm
response = chain.invoke({"context": context, "question": query})
print(response.content)
```

This is the basic idea behind a lot of RAG setups with LangChain.

---

## 8. How to go further from here

To deepen your skills:

- **Beginner tutorials:** There are step-by-step LangChain tutorials that start with model calls, prompt templates, then move to chains and RAG use cases.
- **Prompt templates & parsers:** More in-depth guides show how to build reusable prompt templates and parse structured outputs for production apps.
- **End-to-end applications:** Full LangChain tutorials walk through building LLM apps with prompts, chains, memory, tools, and retrieval.

If you tell me your main goal (e.g., “chatbot for my docs”, “code assistant”, “data summarizer”), I can give you a focused mini‑roadmap and sample code just for that use case.