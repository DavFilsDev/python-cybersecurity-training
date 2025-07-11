# cryptography/caesar_cipher.py

"""
Caesar Cipher Example
---------------------
This script demonstrates how to encrypt and decrypt a message using the Caesar cipher technique.
"""

def caesar_encrypt(text, shift):
    """Encrypts the text using a Caesar cipher."""
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    """Decrypts the text using a Caesar cipher."""
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    message = input("🔐 Enter your message: ")
    shift = int(input("🔑 Enter shift value: "))

    encrypted = caesar_encrypt(message, shift)
    print(f"🔒 Encrypted: {encrypted}")

    decrypted = caesar_decrypt(encrypted, shift)
    print(f"🔓 Decrypted: {decrypted}")
