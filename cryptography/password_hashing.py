# cryptography/password_hashing.py

"""
Secure Password Hashing
-----------------------
This script shows two techniques:
1. bcrypt: hashing and verifying passwords with automatic salting
2. PBKDF2 (from hashlib): key derivation with a salt
"""

import bcrypt
import hashlib
import secrets

def hash_password_bcrypt(password):
    """Hashes a password using bcrypt."""
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

def verify_bcrypt(password, hashed):
    """Verifies a password using bcrypt."""
    return bcrypt.checkpw(password.encode(), hashed)

def hash_password_pbkdf2(password, salt=None):
    """Hashes a password using PBKDF2 with SHA-256."""
    if salt is None:
        salt = secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)
    return salt, dk

if __name__ == "__main__":
    password = input("🔐 Enter a password: ")

    # Bcrypt example
    bcrypt_hash = hash_password_bcrypt(password)
    print(f"\n🔒 Bcrypt Hash: {bcrypt_hash.decode()}")

    valid = verify_bcrypt(password, bcrypt_hash)
    print(f"✅ Password valid (bcrypt): {valid}")

    # PBKDF2 example
    salt, pbkdf2_hash = hash_password_pbkdf2(password)
    print(f"\n🧂 Salt (PBKDF2): {salt.hex()}")
    print(f"🔒 PBKDF2 Hash: {pbkdf2_hash.hex()}")
