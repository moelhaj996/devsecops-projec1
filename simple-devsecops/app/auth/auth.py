from flask import Blueprint, request, jsonify, session, g
import functools
import hashlib
import os
import uuid
from security import validate_username, validate_email

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# In-memory user store (in a real app, use a database)
users = {}

# In-memory token store (in a real app, use a database or Redis)
tokens = {}

def hash_password(password, salt=None):
    """Hash a password with a salt using SHA-256"""
    if salt is None:
        salt = os.urandom(32).hex()
    
    # In a real app, use a proper password hashing library like bcrypt
    hashed = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed, salt

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validate required fields
    if not all(k in data for k in ('username', 'email', 'password')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    username = data['username']
    email = data['email']
    password = data['password']
    
    # Validate input format
    if not validate_username(username):
        return jsonify({'error': 'Invalid username format'}), 400
    
    if not validate_email(email):
        return jsonify({'error': 'Invalid email format'}), 400
    
    if len(password) < 8:
        return jsonify({'error': 'Password must be at least 8 characters'}), 400
    
    # Check if user already exists
    if username in users:
        return jsonify({'error': 'Username already exists'}), 409
    
    # Hash the password
    hashed_password, salt = hash_password(password)
    
    # Store the user
    users[username] = {
        'email': email,
        'password_hash': hashed_password,
        'salt': salt
    }
    
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Validate required fields
    if not all(k in data for k in ('username', 'password')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    username = data['username']
    password = data['password']
    
    # Check if user exists
    if username not in users:
        return jsonify({'error': 'Invalid credentials'}), 401
    
    # Verify password
    user = users[username]
    hashed_password, _ = hash_password(password, user['salt'])
    
    if hashed_password != user['password_hash']:
        return jsonify({'error': 'Invalid credentials'}), 401
    
    # Generate token
    token = str(uuid.uuid4())
    tokens[token] = username
    
    return jsonify({'token': token}), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()
    
    if 'token' not in data:
        return jsonify({'error': 'Token required'}), 400
    
    token = data['token']
    
    # Remove token if it exists
    if token in tokens:
        del tokens[token]
    
    return jsonify({'message': 'Logged out successfully'}), 200

def login_required(view):
    """Decorator to require authentication for a view"""
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        # Get token from Authorization header
        auth_header = request.headers.get('Authorization')
        
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'error': 'Authentication required'}), 401
        
        token = auth_header.split(' ')[1]
        
        if token not in tokens:
            return jsonify({'error': 'Invalid or expired token'}), 401
        
        # Set current user
        g.current_user = tokens[token]
        
        return view(*args, **kwargs)
    
    return wrapped_view

def get_current_user():
    """Get the current authenticated user"""
    return g.get('current_user')