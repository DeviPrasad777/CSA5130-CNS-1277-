import numpy as np

def prepare_message(message):
    message = message.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    # If the message length is not a multiple of 2, pad it with 'X'
    if len(message) % 2 != 0:
        message += 'X'
    return message

def message_to_numbers(message):
    return [ord(char) - ord('A') for char in message]

def numbers_to_message(numbers):
    return ''.join([chr(num + ord('A')) for num in numbers])

def encrypt(message, key):
    # Prepare the message
    message = prepare_message(message)
    # Convert the message to numbers
    numbers = message_to_numbers(message)
    # Convert the key to a 2x2 matrix
    key_matrix = np.array(key).reshape(2, 2)
    # Convert the numbers into pairs of 2 for matrix multiplication
    pairs = [numbers[i:i+2] for i in range(0, len(numbers), 2)]
    # Encrypt each pair
    ciphertext = ""
    for pair in pairs:
        pair_vector = np.array(pair)
        encrypted_pair_vector = np.dot(key_matrix, pair_vector) % 26
        ciphertext += numbers_to_message(encrypted_pair_vector)
    return ciphertext

def decrypt(ciphertext, key):
    # Convert the key to a 2x2 matrix
    key_matrix = np.array(key).reshape(2, 2)
    # Calculate the determinant of the key matrix
    determinant = np.linalg.det(key_matrix)
    # Calculate the modular multiplicative inverse of the determinant
    determinant_inverse = pow(int(round(determinant)) % 26, -1, 26)
    # Calculate the adjugate of the key matrix
    adjugate = np.array([[key_matrix[1][1], -key_matrix[0][1]], [-key_matrix[1][0], key_matrix[0][0]]])
    # Calculate the inverse of the key matrix
    key_inverse = (determinant_inverse * adjugate) % 26
    # Convert the ciphertext to numbers
    numbers = message_to_numbers(ciphertext)
    # Convert the numbers into pairs of 2 for matrix multiplication
    pairs = [numbers[i:i+2] for i in range(0, len(numbers), 2)]
    # Decrypt each pair
    plaintext = ""
    for pair in pairs:
        pair_vector = np.array(pair)
        decrypted_pair_vector = np.dot(key_inverse, pair_vector) % 26
        plaintext += numbers_to_message(decrypted_pair_vector)
    return plaintext

# Define the key matrix
key = [9, 4, 5, 7]

# Encrypt the message
message = "meet me at the usual place at ten rather than eight oclock"
ciphertext = encrypt(message, key)
print("Encrypted message:", ciphertext)

# Decrypt the ciphertext
decrypted_message = decrypt(ciphertext, key)
print("Decrypted message:", decrypted_message)
