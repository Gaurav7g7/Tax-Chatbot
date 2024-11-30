import os
import glob
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import MarkdownTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import UnstructuredMarkdownLoader
import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
def setup_vector_store(markdown_dir):
    markdown_files = glob.glob(os.path.join(markdown_dir, "*.md"))

    if not markdown_files:
        raise ValueError("No markdown files found in the directory.")

    docs = []
    for f in markdown_files:
        try:
            documents = UnstructuredMarkdownLoader(f).load()
            if documents:
                docs.extend(documents)
            else:
                print(f"No documents loaded from {f}")
        except Exception as e:
            print(f"Error loading {f}: {e}")

    if not docs:
        raise ValueError("No documents were successfully loaded.")

    text_splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=100)
    splits = text_splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    embed_splits = embeddings.embed_documents([doc.page_content for doc in splits])

    if not embed_splits:
        raise ValueError("Embeddings generation failed or returned empty results.")

    faiss_index = FAISS.from_embeddings(embed_splits, splits)

    return faiss_index.as_retriever()

if __name__ == "__main__":
    md_directory = r"C:\Users\gaura\PycharmProjects\Tax Agents Chatbot\Md files"
    retriever = setup_vector_store(md_directory)