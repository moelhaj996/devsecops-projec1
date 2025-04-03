from flask import request, abort
import re

class SecurityMiddleware:
    """Middleware to add security headers and perform basic security checks"""
    
    def __init__(self, app):
        self.app = app
        self.app.after_request(self.add_security_headers)
        # Register more security functions as needed
    
    def add_security_headers(self, response):
        """Add security headers to all responses"""
        # Content Security Policy
        response.headers['Content-Security-Policy'] = "default-src 'self'"
        # XSS Protection
        response.headers['X-XSS-Protection'] = '1; mode=block'
        # Content Type Options
        response.headers['X-Content-Type-Options'] = 'nosniff'
        # Frame Options
        response.headers['X-Frame-Options'] = 'DENY'
        # Referrer Policy
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        return response

def setup_request_validation(app):
    """Set up request validation for the Flask app"""
    
    @app.before_request
    def validate_request():
        """Validate incoming requests for basic security issues"""
        # Check for suspicious SQL injection patterns in query parameters
        for key, value in request.args.items():
            if isinstance(value, str) and re.search(r"['\"\\;]|\b(SELECT|INSERT|UPDATE|DELETE|DROP|UNION)\b", value, re.IGNORECASE):
                abort(403, description="Potential SQL injection detected")
        
        # Rate limiting could be implemented here
        
        # More validation as needed