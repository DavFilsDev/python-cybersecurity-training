# basics/hashing_basics.py

"""
Hashing Basics Example
----------------------
This script demonstrates how to generate common hash values (MD5, SHA-1, SHA-256)
from a given input text using Python's hashlib module.
"""

import hashlib

def hash_text(text):
    """Generates and prints MD5, SHA-1, and SHA-256 hashes of the given text."""
    print(f"Original text: {text}")
    print("MD5:     ", hashlib.md5(text.encode()).hexdigest())
    print("SHA-1:   ", hashlib.sha1(text.encode()).hexdigest())
    print("SHA-256: ", hashlib.sha256(text.encode()).hexdigest())

if __name__ == "__main__":
    user_input = input("🔑 Enter a text to hash: ")
    hash_text(user_input)
