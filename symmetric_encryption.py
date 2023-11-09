from cryptography.fernet import Fernet
"""
symmetric encryption
note - Libary to use cryptography.fernet
step 1 - encript
step 2 - file write encripted key
step 3 - read from file encripted key
step 4 - decript key
"""


key = Fernet.generate_key()
#TEST print("encripted key", key)
cipher = Fernet(key)
encrypted_text=cipher.encrypt(b'this is my secret message')
print(encrypted_text)

# cipher= Ferent(key)
