"""
Operations for managing points (vectors) in Qdrant collections.
"""
from qdrant_client import QdrantClient, models
from typing import List, Dict, Any


def insert_points(
    client: QdrantClient,
    collection_name: str,
    points: List[Dict[str, Any]]
) -> None:
    """
    Insert or update points (vectors) in a collection.
    
    Args:
        client: QdrantClient instance
        collection_name: Name of the collection
        points: List of point dictionaries with 'id', 'vector', and 'payload' keys
        
    Example:
        points = [
            {
                "id": 1,
                "vector": [0.1, 0.2, 0.3, 0.4],
                "payload": {"category": "Demo"}
            }
        ]
    """
    point_structs = [
        models.PointStruct(
            id=point["id"],
            vector=point["vector"],
            payload=point.get("payload", {})
        )
        for point in points
    ]
    
    client.upsert(
        collection_name=collection_name,
        points=point_structs
    )
    
    print(f"Inserted {len(point_structs)} points into collection '{collection_name}'")
