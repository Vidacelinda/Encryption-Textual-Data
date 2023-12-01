from cryptography.fernet import Fernet
"""
symmetric encryption
note - Libary to use cryptography.fernet
step 1 - encript
step 2 - file write encripted key
step 3 - read from file encripted key
step 4 - decript key
"""

"""generate file to hold key"""
# key = Fernet.generate_key()
# # TEST print("encripted key", key)
#
# # WRITE key to file to save
# fkey = open("file_key.text", 'wb')
# fkey.write(key)

"""ENCRYPT FILE / Symmtric Encryption"""
# READ key from file
fkey=open("file_key.text",'rb') #read byte
key=fkey.read()

# symetric encryption
cipher=Fernet(key)
print(key)
file_name='excel_test_file.xlsx'
with open(file_name,'rb') as f:
    e_file=f.read()

# encrypt file
encrypted_file=cipher.encrypt(e_file)
# save
with open(file_name+"_encrypted",'wb') as ef:
    ef.write(encrypted_file)



""" TEST 1 / Testing Plain text / cons : does not save key and has to be regenerated """
'''
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
'''