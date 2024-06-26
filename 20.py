from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Function to pad the plaintext
def pad(data):
    padding_length = AES.block_size - len(data) % AES.block_size
    return data + bytes([padding_length] * padding_length)

# Function to encrypt plaintext in ECB mode
def encrypt_ecb(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext))
    return ciphertext

# Function to decrypt ciphertext in ECB mode
def decrypt_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    padding_length = decrypted_data[-1]
    return decrypted_data[:-padding_length]

# Function to encrypt plaintext in CBC mode
def encrypt_cbc(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext))
    return ciphertext

# Function to decrypt ciphertext in CBC mode
def decrypt_cbc(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)
    padding_length = decrypted_data[-1]
    return decrypted_data[:-padding_length]

# Generate random key and IV
key = get_random_bytes(AES.block_size)
iv = get_random_bytes(AES.block_size)

# Example usage
plaintext = b"This is a secret message."
ciphertext_ecb = encrypt_ecb(plaintext, key)
ciphertext_cbc = encrypt_cbc(plaintext, key, iv)

print("ECB mode:")
print("Original plaintext:", plaintext)
print("Ciphertext:", ciphertext_ecb.hex())
print("Decrypted plaintext:", decrypt_ecb(ciphertext_ecb, key))

print("\nCBC mode:")
print("Original plaintext:", plaintext)
print("Ciphertext:", ciphertext_cbc.hex())
print("Decrypted plaintext:", decrypt_cbc(ciphertext_cbc, key, iv))
