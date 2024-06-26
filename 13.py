import numpy as np

# Convert a string to a vector of numbers based on ASCII values
def string_to_vector(s):
    return [ord(char) - ord('a') for char in s.lower() if char.isalpha()]

# Convert a vector of numbers to a string
def vector_to_string(v):
    return ''.join([chr(num + ord('a')) for num in v])

# Encrypt plaintext using the Hill cipher
def hill_cipher_encrypt(plaintext, key):
    plaintext = string_to_vector(plaintext)
    key = np.array(key)
    plaintext_len = len(plaintext)
    
    # Pad plaintext if necessary
    if plaintext_len % len(key) != 0:
        padding = len(key) - (plaintext_len % len(key))
        plaintext.extend([0] * padding)
    
    plaintext = np.array(plaintext).reshape(-1, len(key))
    ciphertext = []
    
    # Encrypt each block of plaintext
    for block in plaintext:
        ciphertext_block = np.dot(block, key) % 26
        ciphertext.extend(ciphertext_block)
    
    return vector_to_string(ciphertext)

# Decrypt ciphertext using the Hill cipher
def hill_cipher_decrypt(ciphertext, key):
    key = np.linalg.inv(np.array(key)) % 26
    return hill_cipher_encrypt(ciphertext, key)

# Perform known plaintext attack on Hill cipher
def known_plaintext_attack(plaintext, ciphertext):
    plaintext_vec = np.array(string_to_vector(plaintext))
    ciphertext_vec = np.array(string_to_vector(ciphertext))
    
    # Check if plaintext and ciphertext have the same length
    if len(plaintext_vec) != len(ciphertext_vec):
        print("Plaintext and ciphertext lengths do not match.")
        return
    
    # Generate all possible 2x2 matrices
    matrices = []
    for i in range(26):
        for j in range(26):
            for k in range(26):
                for l in range(26):
                    matrix = [[i, j], [k, l]]
                    matrices.append(matrix)
    
    # Try each matrix and check if it produces the given plaintext-ciphertext pair
    for matrix in matrices:
        decrypted_plaintext = hill_cipher_decrypt(ciphertext, matrix)
        if decrypted_plaintext == plaintext:
            return matrix

# Test known plaintext attack
plaintext = "meetmeattheusualplaceattenratherthaneightoclock"
ciphertext = "kpcbpgjkgbpmjoawpbhefsubogbjtfllwfuixtvswnrkvjzq"
key = known_plaintext_attack(plaintext, ciphertext)
if key:
    print("Key found:", key)
    print("Decrypted plaintext:", hill_cipher_decrypt(ciphertext, key))
else:
    print("Key not found.")
