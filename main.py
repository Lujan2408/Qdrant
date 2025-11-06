from qdrant_client import models
from config import get_client
from qdrant_collections import create_collection, get_collection_info, create_payload_index
from operations import insert_points
from search import search_similar_vectors, filtered_search_vectors

def main():
    # Initialize Qdrant client
    client = get_client()
    
    # Define collection name
    collection_name = "movie_categories"
    
    # create_collection(
    #     client=client,
    #     collection_name=collection_name,
    #     vector_size=4
    # )
    
    # Create payload index for Category field (run once after creating collection)
    # create_payload_index(
    #     client=client,
    #     collection_name=collection_name,
    #     field_name="Category",
    #     field_type="keyword"
    # )
    
    # Prepare points to insert
    points_data = [
        {
            "id": 1,
            "vector": [0.1, 0.2, 0.3, 0.4],
            "payload": {"Name": "Jumanji","Category": "Adventure"}
        },
        {
            "id": 2,
            "vector": [0.2, 0.3, 0.4, 0.5],
            "payload": {"Name": "Example Movie","Category": "Drama"}
        },
        {
          "id": 3, 
          "vector": [0.05, 0.15, 0.35, 0.25],
          "payload": {"Name": "Example Movie", "Category": "Action"}
        },
        {
          "id": 4,
          "vector": [0.13, 0.22, 0.13, 0.44],
          "payload": {"Name": "Example Movie 2","Category": "Horror"}
        },
        {
          "id": 5,
          "vector": [0.31, 0.27, 0.32, 0.72],
          "payload": {"Name": "Example Movie 2","Category": "Horror"}
        }
    ]
    
    # Insert vectors into the collection
    insert_points(
        client=client,
        collection_name=collection_name,
        points=points_data
    )
    
    # Retrieve collection details
    get_collection_info(client=client, collection_name=collection_name)
    
    # Perform similarity search
    query_vector = [0.13, 0.2, 0.54, 0.2]
    
    # search_similar_vectors(
    #     client=client,
    #     collection_name=collection_name,
    #     query_vector=query_vector,
    #     limit=3
    # )
    
    #Filtered Search
    filtered_search_vectors (
      client=client,
      collection_name=collection_name,
      query_vector=query_vector,
      limit=1,
      filter_condition=models.Filter(
        must=[models.FieldCondition(key="Category", match=models.MatchValue(value="Horror"))]
      ),
    ) 

if __name__ == "__main__":
    main()