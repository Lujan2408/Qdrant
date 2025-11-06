"""
Collection management for Qdrant.
"""
from qdrant_client import QdrantClient, models


def create_collection(
    client: QdrantClient,
    collection_name: str,
    vector_size: int = 4,
    distance: models.Distance = models.Distance.COSINE
) -> None:
    """
    Create a new collection in Qdrant.
    
    Args:
        client: QdrantClient instance
        collection_name: Name of the collection to create
        vector_size: Dimensionality of the vectors
        distance: Distance metric for similarity search
    """
    client.create_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(
            size=vector_size,
            distance=distance
        )
    )
    
    collections = client.get_collections()
    print(f"Collection '{collection_name}' created. Total collections: {len(collections.collections)}")


def get_collection_info(client: QdrantClient, collection_name: str):
    """
    Retrieve detailed information about a collection.
    
    Args:
        client: QdrantClient instance
        collection_name: Name of the collection
        
    Returns:
        Collection information object
    """
    collection_info = client.get_collection(collection_name)
    print(f"Collection info: {collection_info}")
    return collection_info
