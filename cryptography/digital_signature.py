# cryptography/digital_signature.py

"""
Digital Signature Example
-------------------------
This script demonstrates how to create and verify a digital signature using RSA.
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature

def generate_rsa_keys():
    """Generates an RSA private/public key pair."""
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return private_key, private_key.public_key()

def sign_message(private_key, message):
    """Signs a message using the RSA private key."""
    signature = private_key.sign(
        message.encode(),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, message, signature):
    """Verifies a message signature using the RSA public key."""
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False

if __name__ == "__main__":
    message = input("✉️  Enter a message to sign: ")

    private_key, public_key = generate_rsa_keys()
    signature = sign_message(private_key, message)

    print(f"\n🖊️ Signature (hex): {signature.hex()}")

    valid = verify_signature(public_key, message, signature)
    print(f"✅ Signature valid: {valid}")

    # Optional tampering
    altered = message + "!"
    valid_tampered = verify_signature(public_key, altered, signature)
    print(f"❌ Tampered signature valid: {valid_tampered}")
