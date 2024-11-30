import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import MarkdownTextSplitter
from langchain_openai import ChatOpenAI


os.environ["OPENAI_API_KEY"] = "to be implemented"
markdown_directory = r"C:\Users\gaura\PycharmProjects\Tax Agents Chatbot\md files test"
print("Hello World")
markdown_files = [
    os.path.join(markdown_directory, f)
    for f in os.listdir(markdown_directory)
    if f.endswith(".md")
]
print("Hello World1")

docs = [UnstructuredMarkdownLoader(f).load()[0] for f in markdown_files]
print("Hello World2")

text_splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=100)
splits = text_splitter.split_documents(docs)
print("Hello World3")

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
vectorstore = FAISS.from_documents(splits, embeddings)
print("Hello World4")

retriever = vectorstore.as_retriever()

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)
def rag(user_question):
    retrieved_docs = retriever.get_relevant_documents(user_question)
    context = "\n\n".join(doc.page_content for doc in retrieved_docs)
    formatted_prompt = f"Question: {user_question}\n\nContext: {context}"
    response = llm.invoke(formatted_prompt)
    return response.content

