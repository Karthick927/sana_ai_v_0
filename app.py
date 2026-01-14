from flask import Flask, render_template, request, jsonify
from stt import speech_to_text
from llm import ask_llm
from tts import speak_with_emotion
import threading
import json

app = Flask(__name__)

# Store conversation state
current_response = ""
is_speaking = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Chat endpoint for the AI"""
    global current_response, is_speaking
    
    data = request.json
    user_text = data.get('message', '')
    
    if not user_text:
        return jsonify({'error': 'No message provided'}), 400
    
    try:
        # Get AI response
        ai_text = ask_llm(user_text)
        
        # Mark as speaking and generate audio
        is_speaking = True
        
        # Return response
        return jsonify({
            'response': ai_text,
            'status': 'success'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        is_speaking = False

@app.route('/api/speak', methods=['POST'])
def speak():
    """Endpoint to speak the response"""
    global is_speaking
    
    data = request.json
    text = data.get('text', '')
    emotion = data.get('emotion', 'neutral')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    try:
        is_speaking = True
        speak_with_emotion(text, emotion)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        is_speaking = False

@app.route('/api/models', methods=['GET'])
def get_models():
    """Get available VRM models"""
    models = [
        {'id': 1, 'name': 'Sana', 'path': '/static/models/model_1.vrm'},
        {'id': 3, 'name': 'Model 3', 'path': '/static/models/model_3.vrm'},
    ]
    return jsonify(models)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
