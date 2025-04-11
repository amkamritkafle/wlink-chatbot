# app.py
from flask import Flask, request, jsonify
from models.chatbot import ChatRasa

app = Flask(__name__)

chatbot = ChatRasa()

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if user_message:
        # Get response from Rasa agent
        response = chatbot.get_response(user_message)
        return jsonify({"response": response}), 200
    else:
        return jsonify({"error": "No message provided"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)
