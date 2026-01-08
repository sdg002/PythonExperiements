import dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate

if __name__ == "__main__":
    dotenv.load_dotenv(override=True)
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
    print("--------------------------")
    print(response.content)
