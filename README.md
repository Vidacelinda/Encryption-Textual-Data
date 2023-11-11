# Encryption Textual Data test in python

Character Set Definition:
You define a character set chars, which includes space, punctuation, digits, and uppercase and lowercase letters. This character set represents all the characters that can appear in the input text.

Random Key Generation:
You create a key by copying the chars list and shuffling it using random.shuffle. This key will be used to map the characters from the original message to their corresponding replacements during encryption.

Encryption:
The user is prompted to enter a message to encrypt using input().
The code iterates through each character in the input message (plain_text).
For each character, it finds the index of that character in the chars list.
It then uses this index to look up the corresponding character in the key list and appends it to the cipher_text.

Decryption:
The user is prompted to enter an encrypted message to decrypt using input().
The code iterates through each character in the encrypted message (cipher_text).
For each character, it finds the index of that character in the key list.
It uses this index to look up the corresponding character in the chars list and appends it to the plain_text.

Output:
The original message and the encrypted/decrypted message are printed to the console.
will be updated nov 11,2023
