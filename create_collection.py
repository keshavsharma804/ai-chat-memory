from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
import os

# Load environment variables
QDRANT_URL = os.environ.get("QDRANT_URL")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")

if not QDRANT_URL or not QDRANT_API_KEY:
    print("❌ Missing QDRANT_URL or QDRANT_API_KEY in environment variables.")
    exit()

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    timeout=60
)



COLLECTION_NAME = "chat_memory"

# Check if the collection already exists
exists = client.collection_exists(COLLECTION_NAME)

if exists:
    print(f"ℹ️ Collection '{COLLECTION_NAME}' already exists. Skipping creation.")
else:
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=768,
            distance=Distance.COSINE
        )
    )
    print(f"✅ Collection '{COLLECTION_NAME}' created successfully!")
