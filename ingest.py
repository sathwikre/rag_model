import os
import pickle
import faiss

from pypdf import PdfReader
from sentence_transformers import SentenceTransformer


# -----------------------------
# STEP 1: READ PDF
# -----------------------------
pdf_path = "data/book.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text + "\n"


print("PDF loaded successfully")


# -----------------------------
# STEP 2: SPLIT INTO CHUNKS
# -----------------------------
chunk_size = 1000
overlap = 200

chunks = []

start = 0

while start < len(text):
    end = start + chunk_size

    chunk = text[start:end]

    chunks.append(chunk)

    start += chunk_size - overlap


print(f"Created {len(chunks)} chunks")


# -----------------------------
# STEP 3: CREATE EMBEDDINGS
# -----------------------------
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embeddings = model.encode(
    chunks,
    show_progress_bar=True
)

print("Embeddings created")


# -----------------------------
# STEP 4: CREATE VECTORSTORE
# -----------------------------
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

os.makedirs("vectorstore", exist_ok=True)

faiss.write_index(
    index,
    "vectorstore/faiss_index.bin"
)

with open(
    "vectorstore/chunks.pkl",
    "wb"
) as f:
    pickle.dump(chunks, f)


print("Vector database saved successfully")