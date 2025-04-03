from .db import db
import hashlib
import os
from datetime import datetime

class User(db.Model):
    """User model for authentication"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    salt = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)
    
    def set_password(self, password):
        """Hash a password with a salt using SHA-256"""
        # In a real app, use a proper password hashing library like bcrypt
        self.salt = os.urandom(32).hex()
        self.password_hash = hashlib.sha256((password + self.salt).encode()).hexdigest()
    
    def check_password(self, password):
        """Check if the provided password matches the stored hash"""
        hashed = hashlib.sha256((password + self.salt).encode()).hexdigest()
        return hashed == self.password_hash
    
    def to_dict(self):
        """Convert user to dictionary (excluding sensitive fields)"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }