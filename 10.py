def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")  # Replace J with I
    key_set = set(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # No J in Playfair
    matrix = []
    for char in key_set:
        if char in alphabet:
            alphabet = alphabet.replace(char, "")
            matrix.append(char)
    for char in alphabet:
        matrix.append(char)
    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def display_playfair_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

key = "MFHIJKUNOPQZVWXYZELARGDSTBC"
playfair_matrix = generate_playfair_matrix(key)
display_playfair_matrix(playfair_matrix)
