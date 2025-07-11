# cryptography/aes_encryption.py

"""
AES Encryption Example
----------------------
This script demonstrates how to encrypt and decrypt a message using AES (Advanced Encryption Standard).
Library used: cryptography
"""

from cryptography.fernet import Fernet

def generate_key():
    """Generates a secure random key."""
    return Fernet.generate_key()

def encrypt_message(message, key):
    """Encrypts a message using the given key."""
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    return encrypted

def decrypt_message(encrypted_message, key):
    """Decrypts an encrypted message using the given key."""
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_message).decode()
    return decrypted

if __name__ == "__main__":
    key = generate_key()
    print(f"🔑 Generated Key: {key.decode()}")

    message = input("🔐 Enter the message to encrypt: ")
    encrypted = encrypt_message(message, key)
    print(f"🔒 Encrypted: {encrypted.decode()}")

    decrypted = decrypt_message(encrypted, key)
    print(f"🔓 Decrypted: {decrypted}")
