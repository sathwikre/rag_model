# 📚 Book RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF book. The system extracts text from the book, converts it into vector embeddings, stores them in a FAISS vector database, retrieves relevant content for user queries, and uses Google's Gemini model to generate responses.

---

# Project Overview

This project allows users to upload a book (PDF) and ask questions through a chatbot interface.

The chatbot:

- Reads the PDF book
- Splits the content into smaller chunks
- Converts chunks into embeddings
- Stores embeddings in FAISS
- Retrieves relevant chunks for a question
- Sends retrieved context to Gemini
- Generates an answer

If the answer is not found in the book, the chatbot can optionally use Gemini's general knowledge.

---

# Features

✅ PDF-based Question Answering

✅ Semantic Search using Vector Embeddings

✅ FAISS Vector Database

✅ Gemini-powered Responses

✅ Flask Web Interface

✅ Retrieval-Augmented Generation (RAG)

✅ Easy to Extend for Multiple Books

---

# Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| Flask | Web Framework |
| FAISS | Vector Database |
| Sentence Transformers | Embedding Generation |
| PyPDF | PDF Text Extraction |
| Gemini API | Answer Generation |
| HTML/CSS/JavaScript | Frontend Interface |

---

# Project Structure

book-rag/

├── data/

│   └── book.pdf

│

├── templates/

│   └── index.html

│

├── vectorstore/

│   ├── faiss_index.bin

│   └── chunks.pkl

│

├── ingest.py

├── chatbot.py

├── app.py

├── requirements.txt

└── README.md

---

# File Explanation

## data/book.pdf

Contains the source book.

Example:

data/book.pdf

This file acts as the knowledge base for the chatbot.

---

## ingest.py

Purpose:

Processes the PDF and creates the vector database.

Responsibilities:

1. Read PDF
2. Extract text
3. Split text into chunks
4. Generate embeddings
5. Store embeddings in FAISS
6. Save chunks for retrieval

Run:

```bash
python ingest.py
```

Output:

```text
PDF loaded successfully
Embeddings created
Vector database saved successfully
```

---

## vectorstore/

Stores processed knowledge.

Contains:

### faiss_index.bin

Stores vector embeddings.

Example:

```
Chunk 1 → Vector
Chunk 2 → Vector
Chunk 3 → Vector
```

### chunks.pkl

Stores original chunk text.

Example:

```
Chunk 1 Text
Chunk 2 Text
Chunk 3 Text
```

---

## chatbot.py

Main AI engine.

Responsibilities:

1. Load FAISS index
2. Load chunks
3. Convert user question into embedding
4. Search similar chunks
5. Build context
6. Send context to Gemini
7. Return answer

Example Flow:

Question

↓

Embedding

↓

FAISS Search

↓

Relevant Chunks

↓

Gemini

↓

Answer

---

## app.py

Flask backend server.

Responsibilities:

- Serve webpage
- Receive questions
- Call chatbot
- Return responses

Routes:

### Home Page

```
/
```

Loads:

```
index.html
```

### Chat Endpoint

```
/chat
```

Receives:

```json
{
  "message":"What is Quantum Computing?"
}
```

Returns:

```json
{
  "answer":"Quantum Computing is..."
}
```

---

## templates/index.html

Frontend UI.

Contains:

- Chat box
- Input field
- Send button
- JavaScript fetch requests

Allows users to communicate with the chatbot through a browser.

---

# How RAG Works

Traditional Chatbot:

Question

↓

LLM

↓

Answer

Problem:

May hallucinate or provide incorrect information.

---

RAG Chatbot:

Question

↓

Convert to Embedding

↓

Search Vector Database

↓

Retrieve Relevant Chunks

↓

Send Context + Question to LLM

↓

Answer

This ensures answers are grounded in the book content.

---

# Workflow Diagram

PDF Book

↓

Text Extraction

↓

Chunking

↓

Embedding Generation

↓

FAISS Storage

↓

User Question

↓

Question Embedding

↓

Similarity Search

↓

Relevant Chunks

↓

Gemini

↓

Final Answer

---

# Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Step 1: Process the Book

Place PDF inside:

```
data/book.pdf
```

Run:

```bash
python ingest.py
```

This creates:

```
vectorstore/faiss_index.bin
vectorstore/chunks.pkl
```

---

# Step 2: Configure Gemini API

Inside chatbot.py:

```python
genai.configure(
    api_key="YOUR_API_KEY"
)
```

Replace with your Gemini API key.

---

# Step 3: Start the Application

Run:

```bash
python app.py
```

Output:

```text
Running on:
http://127.0.0.1:5000
```

Open in browser:

```
http://127.0.0.1:5000
```

---

# Example Questions

- What is Quantum Computing?
- Explain Chapter 2.
- What is Time Complexity?
- Summarize the Introduction.

---

# Future Improvements

### Multiple PDF Support

Allow users to upload multiple books.

### Source Citations

Display exact page numbers.

### Chat History

Maintain conversation memory.

### Internet Search Fallback

If answer not found in the book:

Question

↓

Book Search

↓

Not Found

↓

Internet Search

↓

Gemini

↓

Answer

### User Authentication

Support multiple users.

### Advanced Vector Databases

Replace FAISS with:

- ChromaDB
- Pinecone
- Weaviate

---

# Advantages

- Fast Retrieval
- Reduced Hallucination
- Domain-Specific Answers
- Easy to Scale
- Supports Large Documents

---

# Author

Sathwik Reddy

Book RAG Chatbot using Flask, FAISS, Sentence Transformers, and Gemini.