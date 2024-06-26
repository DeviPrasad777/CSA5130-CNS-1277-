import string
from collections import Counter

# Define the English letter frequency
english_letter_frequency = {
    'a': 0.0817, 'b': 0.0149, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270,
    'f': 0.0223, 'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015,
    'k': 0.0077, 'l': 0.0402, 'm': 0.0241, 'n': 0.0675, 'o': 0.0751,
    'p': 0.0193, 'q': 0.0010, 'r': 0.0599, 's': 0.0633, 't': 0.0906,
    'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015, 'y': 0.0197,
    'z': 0.0007
}

# Function to decrypt ciphertext using monoalphabetic substitution cipher with a given key
def decrypt(ciphertext, key):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            plaintext += key[char.lower()]
        else:
            plaintext += char
    return plaintext

# Function to calculate the letter frequency of a string
def calculate_letter_frequency(text):
    text = text.lower()
    letter_count = Counter(char for char in text if char.isalpha())
    total_letters = sum(letter_count.values())
    letter_frequency = {letter: count / total_letters for letter, count in letter_count.items()}
    return letter_frequency

# Function to score plaintext based on letter frequency difference
def score_plaintext(plaintext):
    plaintext_frequency = calculate_letter_frequency(plaintext)
    score = sum(abs(english_letter_frequency[letter] - plaintext_frequency.get(letter, 0)) for letter in string.ascii_lowercase)
    return score

# Function to perform a letter frequency attack on monoalphabetic substitution cipher
def letter_frequency_attack(ciphertext, top_n=10):
    possible_plaintexts = []
    for permutation in permutations(string.ascii_lowercase):
        key = dict(zip(string.ascii_lowercase, permutation))
        decrypted_text = decrypt(ciphertext, key)
        score = score_plaintext(decrypted_text)
        possible_plaintexts.append((decrypted_text, score))
    sorted_plaintexts = sorted(possible_plaintexts, key=lambda x: x[1])
    return sorted_plaintexts[:top_n]

# Example usage
ciphertext = "Wklv lv d phvvdjh ri wkh wklug khdg"
top_n = 5
possible_plaintexts = letter_frequency_attack(ciphertext, top_n)
print(f"Top {top_n} possible plaintexts:")
for i, (plaintext, score) in enumerate(possible_plaintexts, 1):
    print(f"{i}. {plaintext} (Score: {score:.4f})")
