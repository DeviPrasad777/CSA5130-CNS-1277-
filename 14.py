def vigenere_encrypt(plaintext, key):
    ciphertext = ''
    for i, char in enumerate(plaintext):
        shift = key[i % len(key)]
        ciphertext += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ''
    for i, char in enumerate(ciphertext):
        shift = key[i % len(key)]
        plaintext += chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
    return plaintext

def find_key(plaintext, ciphertext):
    key = []
    for i in range(len(plaintext)):
        shift = (ord(ciphertext[i]) - ord(plaintext[i])) % 26
        key.append(shift)
    return key

# Part a: Encrypt plaintext "sendmoremoney" with the key stream [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]
plaintext_a = "sendmoremoney"
key_stream_a = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]
ciphertext_a = vigenere_encrypt(plaintext_a, key_stream_a)
print("Ciphertext:", ciphertext_a)

# Part b: Decrypt ciphertext_a to obtain "cashnotneeded"
plaintext_b = "cashnotneeded"
key_b = find_key(plaintext_b, ciphertext_a)
print("Key for decryption:", key_b)
decrypted_text_b = vigenere_decrypt(ciphertext_a, key_b)
print("Decrypted plaintext using found key:", decrypted_text_b)
