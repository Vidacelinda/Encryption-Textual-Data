import rsa

"""generate a private ande public key and save """
# 1024 bit for testing / recommended to use 2048 for secure RSA
# public_key,private_key=rsa.newkeys(1024)
#
# with open("RSA keys/public.pem","wb") as f:
# # with open("public.pem","wb") as f:
#     #save_pkcs1 algorithm
#     f.write(public_key.save_pkcs1("PEM"))
#
# with open("RSA keys/private.pem","wb") as f:
# # with open("private.pem","wb") as f:
#     f.write(private_key.save_pkcs1("PEM"))



"""Function : generate keys / save in file"""
def generate_key():
    # NOTE: 1024 bit for testing / recommended to use 2048 for a more secure RSA
    public_key , private_key = rsa.newkeys(1024)

    with open("RSA keys/public.pem","wb") as f:
        #save_pkcs1 algorithm
        f.write(public_key.save_pkcs1("PEM"))

    with open("RSA keys/private.pem","wb") as f:
        f.write(private_key.save_pkcs1("PEM"))


"""once you have your generate keys you would want to reuse the keys"""
# with open("RSA keys/public.pem","rb") as f:
#     #when reading the pem format you would have to load it using the same algorithm used when saving they key to the file.
#     public_key = rsa.PublicKey.load_pkcs1(f.read())
#
# with open("RSA keys/private.pem","rb") as f:
#     private_key = rsa.PrivateKey.load_pkcs1(f.read())


"""FUNCTION : call private and puyblic keys"""
def public_key():
    with open("RSA keys/public.pem","rb") as f:
        #when reading the pem format you would have to load it using the same algorithm used when saving they key to the file.
        public_key = rsa.PublicKey.load_pkcs1(f.read())
        return public_key

def private_key():
    with open("RSA keys/private.pem","rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
        return private_key

"""Test 1.1 :encrypt message and save it as a file . see if encrypted message works """
# message = "Taco please"
#
# # encode() converts string into bytes
# encrypted_message = rsa.encrypt(message.encode(),public_key)
#
# # print(encrypted_message)
# with open("RSA encrypted message/encrypted.message", "wb") as f:
#     f.write(encrypted_message)

"""FUNCTION :encrypt message and save it as a file"""
def encrypt(message):
    # message = "Taco please"

    # encode() converts string into bytes
    encrypted_message = rsa.encrypt(message.encode(), public_key())

    # print(encrypted_message)
    with open("RSA encrypted message/encrypted.message", "wb") as f:
        f.write(encrypted_message)

"""test 1.2 :decrypt the encrypted message using private key."""
def decrypt(encrypted_file_path):
    # read encrypted message file
    encrypted_message = open(encrypted_file_path, "rb").read()
    decrypted_message = rsa.decrypt(encrypted_message, private_key())

    print(decrypted_message.decode())

if __name__ == '__main__':
    if input('do you want to generate a key') == 'y':
        generate_key()

    message = "this is my secrete message"
    encrypt(message)

    # give file path
    encrypted_file_path = "RSA encrypted message/encrypted.message"
    decrypt(encrypted_file_path)


""" signature """
# #authentic message from sender
# message="hello this is calvo and my email is mrc@123 "
# # NON-authentic message from sender
# # message="hello im calvo trust me (NOT CALVO) "
#
# signature = rsa.sign(message.encode(),private_key,"SHA-256")
#
# """ create and save signature to a file for the message signed """
# # with open("signature","wb") as f:
# #     f.write(signature)
#
# """read signature from file """
# with open("signature","rb") as f:
#     signature=f.read()
#
# # if it print "SHA-256"
# print(rsa.verify(message.encode(),signature,public_key))
