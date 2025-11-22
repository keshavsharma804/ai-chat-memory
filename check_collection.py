from qdrant_client import QdrantClient
import os

client = QdrantClient(
    url=os.environ["QDRANT_URL"],
    api_key=os.environ["QDRANT_API_KEY"],
)

print("Collections:", client.get_collections())

count = client.count("chat_memory").count
print("Number of vectors stored:", count)
