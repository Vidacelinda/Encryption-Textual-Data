import rsa

"""generate a private ande public key and save """
# 1024 bit for testing / recomemended to use 2048 for secure RSA
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



"""once you have your generate keys you would want to reuse the keys"""
with open("RSA keys/public.pem","rb") as f:
    #when reading the pem format you would have to load it using the same algorithm used when saving they key to the file.
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("RSA keys/private.pem","rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

"""Test 1 : see if encrypted message works """
# message = "Taco please"
#
# # encode() converts string into bytes
# encrypted_message = rsa.encrypt(message.encode(),public_key)
#
# # print(encrypted_message)
# with open("RSA encrypted message/encrypted.message", "wb") as f:
#     f.write(encrypted_message)


encrypted_message = open("RSA encrypted message/encrypted.message", "rb").read()

decrypted_message = rsa.decrypt(encrypted_message,private_key)
print(decrypted_message)