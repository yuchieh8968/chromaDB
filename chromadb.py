import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions

default_ef = embedding_functions.DefaultEmbeddingFunction()

client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet",
                                    persist_directory="db/"
                                ))
collection = client.get_or_create_collection(
    name="mbed4", embedding_function=default_ef
)
documents=[
    "testing,10,java,2,4", 
    "testing,20,python,2,4", 
    "testing,15,java,4,8", 
    "QA,5,java,2,4", 
    "QA,20,python,2,4", 
    "QA,10,java,4,8", 
    "prod,100,java,8,16",
    "prod,200,python,8,16",
    "prod,150,java,16,32",
    "prod,250,python,16,32"]
genres = [
    "vms-testing",
    "aks-testing",
    "vms-testing",
    "vms-QA",
    "aks-QA",
    "vms-QA",
    "vms-prod",
    "aks-prod",
    "vms-prod",
    "aks-prod",
]
collection.update(
     documents=documents,
     ids=[f"id{i}" for i in range(len(documents))],
     metadatas=[{"genres": g} for g in genres]
)

input1 = input("Enter Spec: ")

results = collection.query(
    query_texts=[input1],
    n_results=3
)
print(results["documents"])
print(results["metadatas"])
print(results["distances"])

