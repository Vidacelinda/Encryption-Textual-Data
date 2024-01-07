'''
A signature must have the same public key, private key and message to work properly.
'''
import rsa

"""generate keys / save in file"""
def generate_keys():
    public_key,private_key=rsa.newkeys(1024)
    """ store keys / save keys in RSA signature file"""
    #use ".save_pkcs1" algorithm for the keys
    with open("RSA signature/public_key.pem","wb") as f :
        f.write(public_key.save_pkcs1("PEM"))
    with open("RSA signature/private_key.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))

"""once you have your generate keys you would want to reuse the keys"""

# call public key from saved file
def public_key():
    with open("RSA signature/public_key.pem","rb") as f:
        #when reading the pem format you would have to load it using the same algorithm used when saving they key to the file.
        public_key = rsa.PublicKey.load_pkcs1(f.read())
    return public_key

# call private key from saved file
def private_key():
    with open("RSA signature/private_key.pem","rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    return private_key

# generate and save signature
def generate_signature(message):
    signature = rsa.sign(message.encode(),private_key(),"SHA-256")
    """ create and save signature to a file for the message signed """
    with open("RSA signature/signature","wb") as f:
        f.write(signature)

def signature_verfication(message):
    # read signature from file
    with open("RSA signature/signature","rb") as f:
        signature=f.read()

    # if it print "SHA-256" then its verfied if not then Not verified
    try:
        rsa.verify(message.encode(), signature, public_key())
        print("VERIFIED")
    except (ValueError, rsa.pkcs1.VerificationError) as e:
        print("NOT VERIFIED")


if __name__ == '__main__':
    # generate_keys()
    print("TEST", private_key())

    message = "hello this is calvo and my email is mrc@123 "
    # generate_signature(message)
    # message = "hello this is calvo and my email is mrc@123 " #TEST
    signature_verfication(message)
