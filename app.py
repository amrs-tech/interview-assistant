from flask import Flask, render_template, request, jsonify
from chatbot import call_model_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    # For simplicity, the bot just echoes the user's message.
    # bot_response = f"Echo: {user_message}"
    model_resp = call_model_api(user_message)
    return jsonify({'response': model_resp})

if __name__ == '__main__':
    app.run(debug=True)
