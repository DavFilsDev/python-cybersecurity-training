# cryptography/hashing_advanced.py

"""
Advanced Hashing Example
------------------------
This script demonstrates how to use salt and HMAC for secure hashing.
"""

import hashlib
import hmac
import secrets

def hash_with_salt(password, salt=None):
    """Hashes a password with a salt using SHA-256."""
    if salt is None:
        salt = secrets.token_hex(16)
    combined = salt + password
    hash_result = hashlib.sha256(combined.encode()).hexdigest()
    return salt, hash_result

def generate_hmac(secret_key, message):
    """Generates an HMAC using SHA-256."""
    return hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()

if __name__ == "__main__":
    password = input("🔑 Enter password: ")
    
    salt, salted_hash = hash_with_salt(password)
    print(f"🧂 Salt: {salt}")
    print(f"🔒 Salted Hash: {salted_hash}")

    secret = secrets.token_hex(16)
    message = input("✉️  Enter message to HMAC: ")
    hmac_result = generate_hmac(secret, message)
    print(f"🔐 Secret Key: {secret}")
    print(f"📎 HMAC: {hmac_result}")
