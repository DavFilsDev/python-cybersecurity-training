# cryptography/vigenere_cipher.py

"""
Vigenère Cipher Example
-----------------------
This script demonstrates how to encrypt and decrypt a message using the Vigenère cipher.
"""

def generate_key(message, key):
    """Repeats the key to match the message length."""
    key = list(key)
    if len(message) == len(key):
        return "".join(key)
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(message, key):
    """Encrypts the message using the Vigenère cipher."""
    encrypted = []
    key = generate_key(message, key)

    for m, k in zip(message, key):
        if m.isalpha():
            base = ord('A') if m.isupper() else ord('a')
            shift = (ord(m) - base + ord(k.lower()) - ord('a')) % 26
            encrypted.append(chr(base + shift))
        else:
            encrypted.append(m)

    return "".join(encrypted)

def vigenere_decrypt(cipher, key):
    """Decrypts the message using the Vigenère cipher."""
    decrypted = []
    key = generate_key(cipher, key)

    for c, k in zip(cipher, key):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            shift = (ord(c) - base - (ord(k.lower()) - ord('a'))) % 26
            decrypted.append(chr(base + shift))
        else:
            decrypted.append(c)

    return "".join(decrypted)

if __name__ == "__main__":
    message = input("🔐 Enter your message: ")
    keyword = input("🔑 Enter keyword: ")

    encrypted = vigenere_encrypt(message, keyword)
    print(f"🔒 Encrypted: {encrypted}")

    decrypted = vigenere_decrypt(encrypted, keyword)
    print(f"🔓 Decrypted: {decrypted}")
