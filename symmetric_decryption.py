from cryptography.fernet import Fernet

# open saved key file
def decrypt(file):
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