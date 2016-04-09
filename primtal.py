import math # Imports important mathematical functions like gcd
import random
from saving_prime_ryan import save_primes, primes_in_range # Imports function from other file

readf = open('primtal.txt') #Opens file for reading
appf = open('primtal.txt','a') #Opens file for appending

def find_primes(bits, buffer): #Finds primes within a given range of bits
    start_value = (2**bits)+1
    end_value = (2**(bits+1))-1
    if end_value-start_value > buffer:
        end_value = start_value + buffer
    for i in range(start_value, end_value):
        arr_primes.append(i)
    for number in arr_primes:
        for x in range(2, int(number/2)):
            if(math.gcd(number,x) != 1):
                arr_primes.remove(number)
                arr_primes.insert(0,0)
                break
    while arr_primes[0] == 0:
        arr_primes.remove(0)
    print(arr_primes)

def find_primes2(bits,range): # Finds two primes within a given range of bits and returns them
    prime_list = primes_in_range(bits)
    if prime_list.len() > 5:
        rInt = random.randint(0,prime_list.len()-1)
        firstPrime = prime_list[rInt]
        prime_list.remove(prime_list[rInt])
        rInt = random.randint(0,prime_list.len()-1)
        secondPrime = prime_list[rInt]
        return (firstPrime, secondPrime)
    else:
        save_primes(2**(bits+1))
        find_primes2(bits,range)

def public_key(bits, range): # Returns a public key (n,e) for RSA encryption
    # DO THINGS
    firstPrime, secondPrime = find_primes2(bits, range)
    n = firstPrime * secondPrime
    totient = (firstPrime-1) * (secondPrime-1)
    decoy, e = find_primes2(bits/2, range)
    return (n,e)
def private_key(n,e):
    # DO THINGS, BUT PRIVATELY
