# Encryption Textual Data test in python

## Objective

Algorithm's will be used for a larger libary to test homomorphic encryption .

### Symetric encryption : (100% done)

For the implementation of symmetric and asymmetric encryption we decided to use cryptography which contains a scheme “Fernet” to help build the symmetrical implementation for the early demo of the project. The python Symmetric encryption code has three functions and a main routine for generating a key, encryption and decryption using the Fernet encryption scheme. The `generate_key()` function generates a Fernet key, prints it for reference, and writes it to a file named "file_key.text" for later use. The `encrypt_file(file)` function reads the key from the file, performs symmetric encryption on the specified file (in this case, 'excel_test_file.xlsx'), and saves the encrypted content to a new file with a name prefixed by "encrypted_". The `decrypt_file(file)` function reads the key from the file, uses the Fernet scheme for symmetric decryption on the specified encrypted file, and writes the decrypted content to a new file named 'decrypted_excel_test_file.xlsx'. The `main()` function serves as the entry point, prompting the user to generate a key and then demonstrate the encryption and decryption processes on the specified file. If the user chooses to generate a key, it is created and saved before proceeding with the encryption and decryption operations. 

input a file to be ecnrpterd by a key which creates a cipher text file whcih then will be decrypted by the same key which will produce the original file. Note the key is stored in a key file .

### substitution encryption : (100% done)

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

### Asymmetric encryption : (starting dec ,2024 )

Asymmetric encryption is a cryptographic system that uses a pair of keys for secure communication. The key pair consists of a public key and a private key. I will be doing an implmentation of asymetric encrption on a file. Also known as RSA.
