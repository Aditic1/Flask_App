# functions.py
from langchain.embeddings import HuggingFaceEmbeddings
from langchain import FAISS
from langchain.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

def process_documents(file_path):
    # Load documents
    loader = TextLoader(file_path)
    documents = loader.load()
    
    # Split documents
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = text_splitter.split_documents(documents)
    
    # Generate embeddings
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(documents, embeddings)
    
    return db

def query_faiss(db, query):
    # Convert query to embeddings
    embeddings = HuggingFaceEmbeddings()
    query_embedding = embeddings.embed([query])[0]
    
    # Perform similarity search with FAISS
    results = db.similarity_search(query)
    
    # Return the results
    return results
