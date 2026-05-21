import pickle
import faiss
import google.generativeai as genai

from sentence_transformers import SentenceTransformer


# --------------------------
# Gemini API Configuration
# --------------------------

genai.configure(
    api_key="AIzaSyCQwds-yUH4yG6o1cpsvufhwInNpj8xVR8"
)

llm = genai.GenerativeModel(
    "gemini-2.5-flash"
)


# --------------------------
# Load Embedding Model
# --------------------------

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# --------------------------
# Load Vector Database
# --------------------------

index = faiss.read_index(
    "vectorstore/faiss_index.bin"
)

with open(
    "vectorstore/chunks.pkl",
    "rb"
) as f:
    chunks = pickle.load(f)


# --------------------------
# Main Chat Function
# --------------------------

def ask_question(question):

    # Convert question into embedding

    question_embedding = embedding_model.encode(
        [question]
    )

    # Search top 5 chunks

    distances, indices = index.search(
        question_embedding,
        5
    )

    # Collect context

    context = ""

    for idx in indices[0]:
        context += chunks[idx] + "\n\n"

    # Prompt

    prompt = f"""
You are a helpful assistant.

First try to answer using the provided book context.

If the answer is available in the context, answer from the book.

If the answer is NOT available in the context,
say:

'Answer not found in the book. Using general knowledge.'

Then answer using your own knowledge.

Context:
{context}

Question:
{question}
"""

    response = llm.generate_content(
        prompt
    )

    return response.text


# --------------------------
# Terminal Testing
# --------------------------

if __name__ == "__main__":

    while True:

        question = input("\nAsk Question: ")

        if question.lower() == "exit":
            break

        answer = ask_question(question)

        print("\nAnswer:\n")
        print(answer)