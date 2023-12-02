from cryptography.fernet import Fernet

# CODE FOR STUDYING (IGNORE)
""" TEST 1 / Testing Plain text / cons : does not save key and has to be regenerated """

key = Fernet.generate_key()
# TEST print("encripted key", key)

#symetrical encrption
cipher=Fernet(key)
#ENCRPTION
secret_str='t1 this is my secret message'
print('secret message: ',secret_str)
# encrypt // note
encrypted_text=cipher.encrypt(secret_str.encode())
#.decode() removes -> b''
print(encrypted_text.decode())# ex: $dg#56

#DECRIPTION
orignal_text=cipher.decrypt(encrypted_text)
print(orignal_text.decode()) # ex: hello

# cipher= Ferent(key)
'''


"""TEST 2 / generate Key and save to file to be used and dycrypted later"""
'''
key = Fernet.generate_key()
# TEST print("encripted key", key)

# WRITE key to file to save
fkey = open("file_key.text", 'wb')
fkey.write(key)
