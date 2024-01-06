import rsa

#generate a key pait
public_key,private_key=rsa.newkeys(1024)
with open("RSA keys/public.pem","wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open("RSA keys/private.pem","wb") as f:
    f.write(private_key.save_pkcs1("PEM"))