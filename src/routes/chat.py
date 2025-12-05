from flask import Blueprint, request, jsonify
from src.api.claude_client import ClaudeClient
from src.services.haridwar_knowledge import HaridwarKnowledge

chat_bp = Blueprint('chat', __name__)
claude_client = ClaudeClient()
haridwar_knowledge = HaridwarKnowledge()

@chat_bp.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    # lightweight local grounding to keep it Haridwar-centric
    context = haridwar_knowledge.search(user_message)

    # Ask Claude with Haridwar-focused system prompt and local context
    api_response = claude_client.send_message(user_message, context=context)

    # Fallback to curated local knowledge if Claude fails
    if not api_response:
        place_info = haridwar_knowledge.get_info(user_message)
        return jsonify({'response': place_info})

    return jsonify({'response': api_response})

def setup_chat_route(app):
    app.register_blueprint(chat_bp)