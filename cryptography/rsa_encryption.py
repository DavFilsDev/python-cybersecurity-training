# cryptography/rsa_encryption.py

"""
RSA Encryption Example
----------------------
This script demonstrates how to generate RSA keys, encrypt, and decrypt a message.
"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

def generate_rsa_keys():
    """Generates an RSA private/public key pair."""
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_message(public_key, message):
    """Encrypts a message using the RSA public key."""
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    return encrypted

def decrypt_message(private_key, encrypted_message):
    """Decrypts the encrypted message using the RSA private key."""
    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    return decrypted.decode()

if __name__ == "__main__":
    private_key, public_key = generate_rsa_keys()

    message = input("🔐 Enter the message to encrypt: ")

    encrypted = encrypt_message(public_key, message)
    print(f"🔒 Encrypted: {encrypted.hex()}")

    decrypted = decrypt_message(private_key, encrypted)
    print(f"🔓 Decrypted: {decrypted}")
