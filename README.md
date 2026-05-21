# 📚 Book RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions based on book content using FAISS vector database and Google Gemini AI.

## Features

- 🔍 **Smart Document Retrieval**: Uses FAISS for efficient semantic search
- 🤖 **AI-Powered Responses**: Powered by Google Gemini 2.5 Flash LLM
- 💬 **Modern Web Interface**: Clean and responsive UI with real-time chat
- 📖 **Context-Aware Answers**: Provides book-based answers when available
- ⚡ **Fast Performance**: Optimized vector embeddings with SentenceTransformers

## Project Structure

```
book-rag/
├── app.py                 # Flask web server
├── chatbot.py            # Core RAG chatbot logic
├── ingest.py             # Document ingestion and vector indexing
├── requirements.txt      # Python dependencies
├── data/                 # Input books/documents
├── vectorstore/          # FAISS index and chunks
│   ├── faiss_index.bin  # Vector index
│   └── chunks.pkl       # Document chunks
└── templates/
    └── index.html       # Frontend UI
```

## Prerequisites

- Python 3.8+
- Google Gemini API Key
- pip (Python package manager)

## Installation

1. **Clone/Extract the project**
   ```bash
   cd book-rag
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Google API Key**
   - Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Update the API key in `chatbot.py`:
     ```python
     genai.configure(api_key="YOUR_API_KEY_HERE")
     ```

## Usage

### 1. Prepare Your Book Data

Place your book files (`.txt`, `.pdf`, etc.) in the `data/` directory.

### 2. Ingest Documents

Run the ingestion script to process documents and create vector embeddings:

```bash
python ingest.py
```

This will:
- Read documents from the `data/` folder
- Split them into chunks
- Generate embeddings using SentenceTransformers
- Create FAISS index in `vectorstore/`

### 3. Run the Chatbot

**Terminal Mode** - Interactive Q&A:
```bash
python chatbot.py
```

Then type your questions:
```
Ask Question: What is the main theme of the book?
```

**Web Mode** - Full UI:
```bash
python app.py
```

Then open your browser to `http://localhost:5000`

## How It Works

1. **Document Ingestion** (`ingest.py`)
   - Splits documents into manageable chunks
   - Converts chunks to vector embeddings
   - Stores in FAISS for fast retrieval

2. **Query Processing** (`chatbot.py`)
   - Converts user question to embedding
   - Searches top 5 similar chunks from FAISS
   - Combines chunks as context

3. **Answer Generation**
   - Sends context + question to Gemini AI
   - Falls back to general knowledge if answer not in book
   - Returns relevant response

4. **Web Interface** (`app.py` + `index.html`)
   - Real-time chat interface
   - Message history
   - Loading indicators
   - Error handling

## Configuration

### Modify Embedding Model

In `chatbot.py` and `ingest.py`, change the model:
```python
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
# Or try: "all-mpnet-base-v2" for better quality
```

### Adjust Search Results

In `chatbot.py`, modify the number of chunks retrieved:
```python
distances, indices = index.search(question_embedding, 5)  # Change 5 to desired number
```

### Change LLM Model

In `chatbot.py`, update the model name:
```python
llm = genai.GenerativeModel("gemini-2.5-flash")
```

## API Endpoints

### POST /chat

Send a question and get an answer.

**Request:**
```json
{
  "message": "What is the main character's motivation?"
}
```

**Response:**
```json
{
  "answer": "Based on the book, the main character's motivation is..."
}
```

## Dependencies

- `google-generativeai` - Gemini API
- `faiss-cpu` - Vector database
- `sentence-transformers` - Embedding model
- `flask` - Web server
- `pickle` - Serialization

Install all with:
```bash
pip install -r requirements.txt
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| API Key Error | Check your Google Gemini API key in `chatbot.py` |
| FAISS Index Not Found | Run `python ingest.py` to create the index |
| Slow Responses | Reduce number of chunks or use CPU-optimized FAISS |
| Memory Issues | Process smaller batches or reduce chunk size in `ingest.py` |

## Performance Tips

- Use `faiss-cpu` for stable performance on most systems
- Adjust chunk size based on available memory
- Larger chunks = better context but slower retrieval
- Smaller chunks = faster but may lose context

## Future Enhancements

- [ ] Multi-document similarity scoring
- [ ] Chat history persistence
- [ ] Custom knowledge base management
- [ ] Advanced filtering and metadata
- [ ] Response quality scoring
- [ ] Web-based admin panel

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, ensure:
1. All dependencies are installed
2. API keys are correctly configured
3. Vector index exists in `vectorstore/`
4. Documents are properly formatted in `data/`

---

**Created with ❤️ for RAG enthusiasts**
