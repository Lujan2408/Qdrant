from qdrant_client import QdrantClient, models 
import os 
from dotenv import load_dotenv

load_dotenv()
client = QdrantClient(url=os.getenv("QDRANT_URL"), api_key=os.getenv("QDRANT_API_KEY"))

collections = client.get_collections()
print(f"Connected to Qdrant Cloud: {len(collections.collections)} collections" )

# define the collection name 
collection_name = "my_first_collection"

# # create the collection with specified vector parameters
# client.create_collection(
#   collection_name=collection_name,
#   vectors_config=models.VectorParams(
#     size = 4, # Dimensionality of the vectors
#     distance = models.Distance.COSINE # Distance metric to use for similarity search
#   )
# )

collections = client.get_collections()
print(f"Collection '{collection_name}' created. Total collections: {len(collections.collections)}")


# Insert points into the collection
points = [
  models.PointStruct(
    id = 1, 
    vector = [0.1, 0.2, 0.3, 0.4],
    payload = {
        "category": "Demo"
      }
  ),
  models.PointStruct(
    id = 2, 
    vector = [0.2, 0.3, 0.4, 0.5],
    payload = {
        "category": "example"
      }
  )
]

# insert vectors into the collection
client.upsert(
  collection_name=collection_name,
  points=points
)

# retrieve collection details
collection_info = client.get_collection(collection_name)
print(f"Collection info:", collection_info)

# Similarity search 

query_vector = [0.08, 0.14, 0.33, 0.28]

search_results = client.query_points(
  collection_name = collection_name,
  query = query_vector,
  limit = 1 # Return the top 1 most similar vector
)

print("Search results:", search_results)