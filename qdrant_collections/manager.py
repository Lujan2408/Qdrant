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


def create_payload_index(
    client: QdrantClient,
    collection_name: str,
    field_name: str,
    field_type: str = "keyword"
) -> None:
    """
    Create a payload index for faster filtering.
    
    Args:
        client: QdrantClient instance
        collection_name: Name of the collection
        field_name: Name of the field to index (e.g., "Category")
        field_type: Type of index - "keyword" for exact match, "integer", "float", "text", etc.
    """
    # Map string types to proper Qdrant schema types
    schema_map = {
        "keyword": models.PayloadSchemaType.KEYWORD,
        "integer": models.PayloadSchemaType.INTEGER,
        "float": models.PayloadSchemaType.FLOAT,
        "text": models.PayloadSchemaType.TEXT,
        "geo": models.PayloadSchemaType.GEO,
        "bool": models.PayloadSchemaType.BOOL
    }
    
    schema = schema_map.get(field_type, models.PayloadSchemaType.KEYWORD)
    
    client.create_payload_index(
        collection_name=collection_name,
        field_name=field_name,
        field_schema=schema
    )
    
    print(f"Payload index created for field '{field_name}' in collection '{collection_name}'")


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
