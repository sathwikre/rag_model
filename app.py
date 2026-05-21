from flask import Flask, render_template, request, jsonify
from chatbot import ask_question

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    question = data.get("message")

    answer = ask_question(question)

    return jsonify({
        "answer": answer
    })


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )