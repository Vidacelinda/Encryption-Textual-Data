from cryptography.fernet import Fernet
"""
symmetric encryption
note - Libary to use cryptography.fernet
step 1 - encript
step 2 - file write encripted key
step 3 - read from file encripted key
step 4 - decript key
"""


# key = Fernet.generate_key()
#TEST print("encripted key", key)

# #WRITE key to file to save
# fkey=open("file_key.text",'wb')
# fkey.write(key)

#READ key from file
# fkey=open("file_key.text",'rb')
# key=fkey.read()
# cipher=Fernet(key)
# print(key)


"""TEST 1 """
key = Fernet.generate_key()
# TEST print("encripted key", key)

cipher=Fernet(key)
#ENCRPTION
encrypted_text=cipher.encrypt(b't1 this is my secret message')
#.decode() removes -> b''
print(encrypted_text.decode())# ex: $dg#56

#DECRIPTION
orignal_text=cipher.decrypt(encrypted_text)
print(orignal_text.decode())# ex: hello

# cipher= Ferent(key)
