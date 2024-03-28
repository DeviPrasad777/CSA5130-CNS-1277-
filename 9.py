def generate_playfair_table(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Note: No 'J' in Playfair
    key = key.upper().replace("J", "I")
    key_set = set(key)
    table = [[None] * 5 for _ in range(5)]
    row, col = 0, 0
    for letter in key:
        table[row][col] = letter
        key_set.remove(letter)
        col += 1
        if col == 5:
            col = 0
            row += 1
    for letter in alphabet:
        if letter not in key_set:
            table[row][col] = letter
            col += 1
            if col == 5:
                col = 0
                row += 1
    return table

def find_letter_positions(table, letter):
    for i, row in enumerate(table):
        for j, char in enumerate(row):
            if char == letter:
                return i, j

def playfair_decrypt(ciphertext, key):
    table = generate_playfair_table(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row_a, col_a = find_letter_positions(table, a)
        row_b, col_b = find_letter_positions(table, b)
        if row_a == row_b:  # Same row
            plaintext += table[row_a][(col_a - 1) % 5] + table[row_b][(col_b - 1) % 5]
        elif col_a == col_b:  # Same column
            plaintext += table[(row_a - 1) % 5][col_a] + table[(row_b - 1) % 5][col_b]
        else:  # Rectangle
            plaintext += table[row_a][col_b] + table[row_b][col_a]
    return plaintext

def brute_force_decrypt(ciphertext):
    keywords = ["PT109", "PATROL", "KENNEDY", "DESTROYER", "JFK", "NAVY", "BOAT", "SUNK"]
    for key in keywords:
        plaintext = playfair_decrypt(ciphertext, key)
        print(f"Using keyword '{key}': {plaintext}")

ciphertext = "KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY CAJPO BOTEI ZONTX BYBNT GONEY CUZWR GDSON SXBOU YWRHE BAAHY USEDQ"
brute_force_decrypt(ciphertext)
