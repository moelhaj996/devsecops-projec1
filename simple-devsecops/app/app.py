from flask import Flask, request, jsonify, g
import os
from security import SecurityMiddleware, setup_request_validation, sanitize_input
from app.auth import auth_bp, login_required

app = Flask(__name__)

# Configure secret key for sessions
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24).hex())

# Apply security middleware
SecurityMiddleware(app)
setup_request_validation(app)

# Register blueprints
app.register_blueprint(auth_bp)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Secure API"})

@app.route('/api/data')
def get_data():
    # Secure implementation - no sensitive data exposure
    return jsonify({"data": "This is secure data"})

@app.route('/api/protected')
@login_required
def protected():
    # This endpoint is only accessible to authenticated users
    return jsonify({"message": f"Hello, {g.current_user}! This is protected data."})

@app.route('/api/echo', methods=['POST'])
def echo():
    # Input validation to prevent injection attacks
    data = request.get_json()
    if not data or not isinstance(data.get('message'), str):
        return jsonify({"error": "Invalid input"}), 400
    
    # Sanitize input to prevent XSS
    message = sanitize_input(data.get('message'))
    
    return jsonify({"echo": message})

if __name__ == '__main__':
    # Secure configuration - don't use debug in production
    debug_mode = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=debug_mode)