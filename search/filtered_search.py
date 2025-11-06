from qdrant_client import QdrantClient, models

def filtered_search_vectors(
    client: QdrantClient,
    collection_name: str,
    query_vector: list,
    limit: int,
    filter_condition = models.Filter()
):
  
  filtered_results = client.query_points(
    collection_name=collection_name,
    query=query_vector,
    limit=limit,
    query_filter=filter_condition
  )
  
  print(f"Filtered search results: {filtered_results}")
  return filtered_results