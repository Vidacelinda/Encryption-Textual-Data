import rsa


"""Function : generate keys / save in file"""
def generate_key():
    # NOTE: 1024 bit for testing / recommended to use 2048 for a more secure RSA
    public_key , private_key = rsa.newkeys(1024)
    # print('private key generated',private_key)
    with open("RSA keys/public.pem","wb") as f:
        #save_pkcs1 algorithm
        f.write(public_key.save_pkcs1("PEM"))

    with open("RSA keys/private.pem","wb") as f:
        f.write(private_key.save_pkcs1("PEM"))


"""once you have your generate keys you would want to reuse the keys"""
# FUNCTION : call private and public keys
def public_key():
    with open("RSA keys/public.pem","rb") as f:
        # when reading the pem format you would have to load it using the same algorithm used when saving they key to the file.
        public_key = rsa.PublicKey.load_pkcs1(f.read())
        return public_key

def private_key():
    with open("RSA keys/private.pem","rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
        # print('private key :',private_key)
        return private_key



"""FUNCTION :encrypt message and save it as a file"""
def encrypt(message,public_key):
    # message = "Taco please"

    # encode() converts string into bytes
    encrypted_message = rsa.encrypt(message.encode(), public_key)

    # print(encrypted_message)
    with open("RSA encrypted message/encrypted.message", "wb") as f:
        f.write(encrypted_message)

"""test 1.2 :decrypt the encrypted message using private key."""
def decrypt(encrypted_file_path, private_key):
    # read encrypted message file
    encrypted_message = open(encrypted_file_path, "rb").read()
    decrypted_message = rsa.decrypt(encrypted_message, private_key)

    print("decrypted message : ",decrypted_message.decode())

if __name__ == '__main__':
    print('1#  User 1 has: private_key and public_key  \n2# User 2 will send a message to be encrpted by using User 1 public key \n3# User 1 will use his private key to encrypt User 2 message \n')
    if input('do you want to generate a key :') == 'y':
        generate_key()
    print('\n### Your User 2 sending a message ###')
    message = input('Enter message:')

    print("message encrypted using User_1's public key")
    encrypt(message, public_key())

    # give file path
    encrypted_file_path = "RSA encrypted message/encrypted.message"
    print('\n### Your User 1 receiving a message: ###')
    print("message decrypted using User_1's public key")
    # decrypted file prints message
    decrypt(encrypted_file_path, private_key())


