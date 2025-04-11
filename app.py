from flask import Flask, render_template, request
from models.conversation_handler import handle_input
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chatbot_template.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    customer_id = request.form['customer_id']  # Pass customer ID through the frontend
    response = handle_input(user_input, customer_id)
    return response

if __name__ == '__main__':
    app.run(debug=True)
