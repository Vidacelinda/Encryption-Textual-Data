from cryptography.fernet import Fernet
"""
symmetric encryption
note - Libary used cryptography.fernet
step 1 - encript
step 2 - file write the encripted key
step 3 - read from file encripted key
step 4 - decript key
"""




"""Generate file to hold key"""
def generate_file():
    # generate key
    key = Fernet.generate_key()
    print("encripted key : ", key)

    # WRITE key to file to save and use later
    fkey = open("file_key.text", 'wb')
    fkey.write(key)

"""ENCRYPT FILE / Symmtric Encryption"""
def encrypt_file(file):
    # READ key from "file_key"
    fkey=open("file_key.text", 'rb') #read byte
    key=fkey.read()

    # symetric encryption
    cipher=Fernet(key)
    # print(key) #TEST

    file_name=file
    with open(file_name,'rb') as f:
        e_file=f.read()

    # encrypt file
    encrypted_file=cipher.encrypt(e_file)

    # save encrypted (write to file )
    with open(file_name+"_encrypted",'wb') as ef:
        ef.write(encrypted_file)

# open saved key file
def decrypt_file(file):
    fkey = open("file_key.text", 'rb')
    key=fkey.read()
    # use fernet scheme
    cipher=Fernet(key)
    # read saved encrypted_data
    with open('excel_test_file.xlsx_encrypted','rb') as df:
        encrypted_data=df.read()
    # Decrypt the encrypted_data to obtain the original data.
    decrypted_file=cipher.decrypt(encrypted_data)
    # make a new file showing the decrpted file
    with open('decrypted_excel_test_file.xlsx','wb') as df:
        df.write(decrypted_file)


def main():
    print("Main function")
    if (input('generate key ? enter y/n ').lower())=='y':
        generate_file()

    encrypt_file('excel_test_file.xlsx')
    decrypt_file('excel_test_file.xlsx')


if __name__ == '__main__':
    main()








# CODE FOR STUDYING (IGNORE)
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