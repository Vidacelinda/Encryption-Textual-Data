import random

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



