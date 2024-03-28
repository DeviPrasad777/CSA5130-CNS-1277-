from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

def pad(data):
    padding_length = 8 - len(data) % 8
    return data + bytes([padding_length] * padding_length)

def encrypt_cbc_3des(plaintext, key, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext))
    return ciphertext

def decrypt_cbc_3des(ciphertext, key, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)
    padding_length = decrypted_data[-1]
    return decrypted_data[:-padding_length]

# Example usage
plaintext = b"This is a secret message"
key = get_random_bytes(24)  # 3DES key size is 24 bytes (192 bits)
iv = get_random_bytes(8)     # Initialization vector size is 8 bytes (64 bits)

ciphertext = encrypt_cbc_3des(plaintext, key, iv)
print("Ciphertext:", ciphertext.hex())

decrypted_text = decrypt_cbc_3des(ciphertext, key, iv)
print("Decrypted plaintext:", decrypted_text.decode())
