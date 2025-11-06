"""
Client configuration for Qdrant connection.
"""
from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv


def get_client() -> QdrantClient:
    """
    Initialize and return a Qdrant client with credentials from environment variables.
    
    Returns:
        QdrantClient: Configured Qdrant client instance
    """
    load_dotenv()
    
    url = os.getenv("QDRANT_URL")
    api_key = os.getenv("QDRANT_API_KEY")
    
    if not url or not api_key:
        raise ValueError("QDRANT_URL and QDRANT_API_KEY must be set in .env file")
    
    client = QdrantClient(url=url, api_key=api_key)
    
    # Verify connection
    collections = client.get_collections()
    print(f"Connected to Qdrant Cloud: {len(collections.collections)} collections")
    
    return client
