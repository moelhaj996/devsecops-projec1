import re
import html

def sanitize_input(input_string):
    """Sanitize user input to prevent XSS attacks"""
    if not isinstance(input_string, str):
        return input_string
    
    # HTML escape the input
    sanitized = html.escape(input_string)
    return sanitized

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_username(username):
    """Validate username format"""
    # Only allow alphanumeric characters, underscore, and hyphen
    pattern = r'^[a-zA-Z0-9_-]{3,16}$'
    return bool(re.match(pattern, username))