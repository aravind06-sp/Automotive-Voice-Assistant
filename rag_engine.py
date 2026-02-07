import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# -------------------------
# Load Embedding Model
# -------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# -------------------------
# Load Knowledge Base
# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KNOWLEDGE_PATH = os.path.join(BASE_DIR, "knowledge.txt")

with open(KNOWLEDGE_PATH, "r", encoding="utf-8") as f:
    docs = [line.strip() for line in f.readlines()]

# -------------------------
# Create Embeddings
# -------------------------
embeddings = model.encode(docs)
dimension = embeddings.shape[1]

# -------------------------
# Build FAISS Index
# -------------------------
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# -------------------------
# RAG Function
# -------------------------
def answer_question(query):
    query_vec = model.encode([query])
    _, idx = index.search(np.array(query_vec), 1)
    return docs[idx[0][0]]
