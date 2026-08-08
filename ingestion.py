import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

load_dotenv()

if __name__ == "__main__":
    loader = TextLoader("data/mediumblog1.txt", encoding="utf-8")   
    document = loader.load()

    print("Splitting...")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(f"created {len(texts)} chunks")



    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("clearing existing index...")
    pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
    index = pc.Index(os.environ.get("INDEX_NAME"))
    index.delete(delete_all=True)

    print("ingesting...")
    PineconeVectorStore.from_documents(
        texts,
        embeddings,
        index_name=os.environ.get("INDEX_NAME")
    )
    print("finish")