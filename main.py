from config import get_client
from qdrant_collections import create_collection, get_collection_info
from operations import insert_points
from search import search_similar_vectors

def main():
    # Initialize Qdrant client
    client = get_client()
    
    # Define collection name
    collection_name = "my_first_collection"
    
    # Create collection (uncomment to create a new collection)
    # create_collection(
    #     client=client,
    #     collection_name=collection_name,
    #     vector_size=4
    # )
    
    # Prepare points to insert
    points_data = [
        {
            "id": 1,
            "vector": [0.1, 0.2, 0.3, 0.4],
            "payload": {"category": "Demo"}
        },
        {
            "id": 2,
            "vector": [0.2, 0.3, 0.4, 0.5],
            "payload": {"category": "example"}
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
    query_vector = [0.08, 0.14, 0.33, 0.28]
    search_similar_vectors(
        client=client,
        collection_name=collection_name,
        query_vector=query_vector,
        limit=1
    )

if __name__ == "__main__":
    main()