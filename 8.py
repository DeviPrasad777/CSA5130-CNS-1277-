#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define ALPHABET_SIZE 26
void generateCipherSequence(char keyword[], char cipherSequence[]) {
    int keywordLength = strlen(keyword);
    int alphabet[ALPHABET_SIZE] = {0};
    for (int i = 0; i < keywordLength; i++) {
        if (isalpha(keyword[i])) {
            int index = toupper(keyword[i]) - 'A';
            alphabet[index] = 1;
        }
    }
    int index = 0;
    for (int i = 0; i < keywordLength; i++) {
        if (isalpha(keyword[i])) {
            cipherSequence[index++] = toupper(keyword[i]);
            alphabet[toupper(keyword[i]) - 'A'] = 2; // Marking used letters
        }
    }
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        if (alphabet[i] == 0) {
            cipherSequence[index++] = 'A' + i;
        }
    }
    cipherSequence[index] = '\0';
}
void encrypt(char plaintext[], char cipherSequence[], char ciphertext[]) {
    int length = strlen(plaintext);

    for (int i = 0; i < length; i++) {
        if (isalpha(plaintext[i])) {
            char plainChar = toupper(plaintext[i]);
            int index = plainChar - 'A';
            ciphertext[i] = cipherSequence[index];
        } else {
            ciphertext[i] = plaintext[i];
        }
    }
    ciphertext[length] = '\0';
}
int main() {
    char keyword[] = "CIPHER";
    char cipherSequence[ALPHABET_SIZE + 1];
    char plaintext[1000];
    char ciphertext[1000];
    printf("Enter the plaintext: ");
    fgets(plaintext, sizeof(plaintext), stdin);
    generateCipherSequence(keyword, cipherSequence);
    encrypt(plaintext, cipherSequence, ciphertext);
    printf("Cipher Sequence: %s\n", cipherSequence);
    printf("Ciphertext: %s\n", ciphertext);
    return 0;
}
    
