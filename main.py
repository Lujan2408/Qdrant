from qdrant_client import QdrantClient, models 
import os 
from dotenv import load_dotenv

load_dotenv()
client = QdrantClient(url=os.getenv("QDRANT_URL"), api_key=os.getenv("QDRANT_API_KEY"))

collections = client.get_collections()
print(f"Connected to Qdrant Cloud: {len(collections.collections)} collections" )

# define the collection name 
collection_name = "my_first_collection"

# create the collection with specified vector parameters
client.create_collection(
  collection_name=collection_name,
  vectors_config=models.VectorParams(
    size = 4, # Dimensionality of the vectors
    distance = models.Distance.COSINE # Distance metric to use for similarity search
  )
)

collections = client.get_collections()
print(f"Collection '{collection_name}' created. Total collections: {len(collections.collections)}")