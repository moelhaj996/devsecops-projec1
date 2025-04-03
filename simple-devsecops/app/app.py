from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Secure API"})

@app.route('/api/data')
def get_data():
    # Secure implementation - no sensitive data exposure
    return jsonify({"data": "This is secure data"})

@app.route('/api/echo', methods=['POST'])
def echo():
    # Input validation to prevent injection attacks
    data = request.get_json()
    if not data or not isinstance(data.get('message'), str):
        return jsonify({"error": "Invalid input"}), 400
    
    # Sanitize input to prevent XSS
    message = data.get('message')
    # In a real app, you would sanitize the input here
    
    return jsonify({"echo": message})

if __name__ == '__main__':
    # Secure configuration - don't use debug in production
    debug_mode = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=debug_mode)