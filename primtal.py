import math # Imports important mathematical functions like gcd
import random
from saving_prime_ryan import save_primes, primes_in_range, in_file # Imports function from other file

readf = open('primtal.txt') #Opens file for reading
appf = open('primtal.txt','a') #Opens file for appending

def find_primes2(bits,range): # Finds two primes within a given range of bits and returns them
    prime_list = primes_in_range(bits)
    if len(prime_list) > 5:
        rInt = random.randint(0,len(prime_list)-1)
        firstPrime = prime_list[rInt]
        prime_list.remove(prime_list[rInt])
        rInt = random.randint(0,len(prime_list)-1)
        secondPrime = prime_list[rInt]
        return (firstPrime, secondPrime)
    else:
        save_primes(bits+1)
        find_primes2(bits,range)

def public_key(bits, range): # Returns a public key (n,e) and Euler's totient for RSA encryption
    # DO THINGS
    firstPrime, secondPrime = find_primes2(bits, range)
    nKey = firstPrime * secondPrime
    totientFunc = (firstPrime-1) * (secondPrime-1)
    eKey,decoy = find_primes2(bits-1, range) #Decoy because find_primes2 returns 2 values - we only need one
    if math.gcd(eKey,totientFunc) == 1:
        return (nKey,eKey,totientFunc)
    else:
        public_key(bits-1,range)

def exteuclidAlg(nKey,eKey): # Returns last number of the Extended Euclidean Algorithm for public key (n,e) to find modular inverse.
    row1 = [nKey,1,0]
    row2 = [eKey,0,1]
    iterations = 0
    while row2[0] != 1:
        k1,k2 = row1[0],row2[0]
        k = math.floor(k1/k2)
        newrow2 = [row1[0]-k*row2[0],row1[1]-k*row2[1], row1[2]-k*row2[2]]
        newrow1 = row2
        row2 = newrow2
        row1 = newrow1
        iterations+=1
    #print(iterations)
    return (row2[2])

def private_key(e,totientFunc): # Returns the private key (n,d) for RSA decryption
    # DO THINGS, BUT PRIVATELY
    deKey = exteuclidAlg(totientFunc,e)
    if deKey < 0:
        deKey += totientFunc
    return deKey

n,e,totient = public_key(16,100)
d = private_key(e,totient)

def encrypt(msg): # Encrypts a message with the public key
    msgE = pow(msg,e,n)
    return msgE

def decrypt(msgE): # Decrypts an encrypted message with the private key
    msgD = pow(msgE,d,n)
    return msgD

encMsg = encrypt(8) # Demonstration of encryption printed to console
print(encMsg)
decMsg = decrypt(encMsg)
print(decMsg)