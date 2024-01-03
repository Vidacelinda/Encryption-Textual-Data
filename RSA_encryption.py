import random
import math

# is number prime
def is_prime(number):
    if number<2:
        return False
    for i in range(2,number // 2+1):
        if number % i== 0:
            return False
    return True
# generate prime number
def generate_prime(min_val,max_val):
    #for the moment gentrate random number until it is prime
    prime =random.randit(min_val,max_val)
    while not is_prime(prime):
        prime=random.randint(min_val,max_val)
    return prime

def mod_inverse(e,phi):
    for d in range(3,phi):
        if (d*e)%phi==1:
            return d
    raise ValueError("mod_invers does not exist")

p,q=generate_prime(1000,5000),generate_prime(1000,5000)
while p==q:
    q=generate_prime(1000,5000)
n=p*q
phi_n=(p-1)*(q-1)

e=random.randint(3,phi_n-1)
while math.gcd(e,phi_n)!=1:
    e=random.randint(3,phi_n-1)

d=mod_inverse(e,phi_n)

print("public key",e)
print("private key",d)
print("n",n)
print("phi of n:",phi_n)
print("p")
