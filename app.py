from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Simple AI responses (rule-based)
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm doing well, thanks!", "Great! How about you?", "I'm good!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["I'm not sure I understand.", "Could you rephrase that?", "Interesting! Tell me more."]
}

def get_ai_response(user_message):
    """Simple AI logic to return a response"""
    message = user_message.lower().strip()

    for key in responses:
        if key in message:
            return random.choice(responses[key])

    return random.choice(responses["default"])

@app.route('/')
def home():
    return jsonify({"message": "Flask AI API is running!"})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    ai_response = get_ai_response(user_message)
    return jsonify({"response": ai_response})

if __name__ == '__main__':
    app.run()