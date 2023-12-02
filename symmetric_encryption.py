from cryptography.fernet import Fernet

"""
1- generate key
2- save generated key to "file_key.text"

Encryption 
3- read key form "file_key.text"
4- use key for the cipher algorithm using Fernet/ ex: cipher=Fernet(key)
5- 
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




