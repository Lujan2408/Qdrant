"""
Similarity search operations in Qdrant collections.
"""
from qdrant_client import QdrantClient
from typing import List


def search_similar_vectors(
    client: QdrantClient,
    collection_name: str,
    query_vector: List[float],
    limit: int = 1
):
    """
    Search for similar vectors in a collection.
    
    Args:
        client: QdrantClient instance
        collection_name: Name of the collection to search
        query_vector: Vector to find similarities for
        limit: Maximum number of results to return
        
    Returns:
        Search results with the most similar vectors
    """
    search_results = client.query_points(
        collection_name=collection_name,
        query=query_vector,
        limit=limit
    )
    
    print(f"Search results: {search_results}")
    return search_results
