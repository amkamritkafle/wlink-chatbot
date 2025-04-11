from flask import Flask, request, jsonify, render_template
from models.chatbot import ChatRasa
import asyncio

app = Flask(__name__)
chatbot = ChatRasa()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if user_message:
        try:
            response = asyncio.run(chatbot.get_response(user_message))
            return jsonify({"response": response}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "No message provided"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)
