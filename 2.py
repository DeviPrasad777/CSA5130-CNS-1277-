import string
import random

def generate_cipher_map():
    plaintext_alphabet = list(string.ascii_lowercase)
    random.shuffle(plaintext_alphabet)
    ciphertext_alphabet = string.ascii_lowercase
    cipher_map = dict(zip(plaintext_alphabet, ciphertext_alphabet))
    return cipher_map

def encrypt(plaintext, cipher_map):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                ciphertext += cipher_map[char]
            else:
                ciphertext += cipher_map[char.lower()].upper()
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, cipher_map):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                plaintext += list(cipher_map.keys())[list(cipher_map.values()).index(char)]
            else:
                plaintext += list(cipher_map.keys())[list(cipher_map.values()).index(char.lower())].upper()
        else:
            plaintext += char
    return plaintext

# Example usage:
plaintext = "Hello, World!"
cipher_map = generate_cipher_map()
encrypted_text = encrypt(plaintext, cipher_map)
print("Encrypted text:", encrypted_text)
decrypted_text = decrypt(encrypted_text, cipher_map)
print("Decrypted text:", decrypted_text)
