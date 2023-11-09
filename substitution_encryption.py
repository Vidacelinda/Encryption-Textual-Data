#Carlo Leiva
#Textual data encryption
# Substitution cipher
import string
import random
# to avoid unknown characters so I put a space
chars = " " + string.punctuation + string.digits + string.ascii_letters
#place them in a list
chars = list(chars) #a b c
key = chars.copy()

#shuffel key randomly
random.shuffle(key) # c a b

#ENCRYPT
plain_text = input("Enter a message to encrypt: ") #abc
cipher_text = "" #c a b

for letter in plain_text:
    index = chars.index(letter) # a:1, b:2 , c:3
    # print(index)
    cipher_text += key[index]   # $:1, f:2 , &:3
    # print(cipher_text+"\n")

print(f"original message : {plain_text}")
print(f"encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)  # $:1, f:2 , &:3
    plain_text += chars[index] # a:1, b:2 , c:3

print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_text}")


#symmetric encryption
#note Libary to use cryptography.fernet
#step 1 encript
#step 2 file write encripted key
#step 3 read from file encripted key
#step 4 decript key