from flask import Flask, request, jsonify, send_from_directory
import openai
import os

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your GPT-3.5 Turbo API key


openai.api_key = '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'
context =[
{"role":"system", "content":"you are Australian Tax Assistant."}]
messages = context

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():    
    user_message = request.json['userMessage']
    messages.append({"role":"user", "content":user_message})
    
    response = openai.ChatCompletion.create( model="gpt-3.5-turbo",  messages=messages)   
      
    chatbot_response = response.choices[0].message["content"] 
    
    return jsonify({'chatbotResponse': chatbot_response})

# Serve static files from the 'static' folder
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
