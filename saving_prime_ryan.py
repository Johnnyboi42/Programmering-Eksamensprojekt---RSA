def in_file(numberino): # Decides if the given number is in the file 'primtal.txt'
    readf = open('primtal.txt')
    readf.seek(0)
    for line in readf:
        if int(line) == numberino:
            return True

def primes_in_range(bit): # Returns a list of the primes in the given bit range
    readtxt = open('primtal.txt')
    prime_list = []
    for line in readtxt:
        if int(line) > 2**bit and int(line) < 2**(bit+1):
            prime_list.append(int(line))
    return prime_list

def save_primes(lim): # Saves primes in file 'primtal.txt' if number is prime and not in file already
    readfile = open('primtal.txt')
    readexpo = open('biggestexponent.txt')
    readexpo.seek(0)
    biggestNum = int(readexpo.readline())
    if biggestNum < lim:
        for number in range(2**biggestNum,2**lim):
            if in_file(number) != True:
                is_prime = True
                readfile.seek(0)
                for line in readfile:
                    if int(line) <= number/2:
                        if number % int(line) == 0:
                            is_prime = False
                            break
                    else:
                        break
                if is_prime:
                    appendf = open('primtal.txt','a') # 'a' for append
                    appendf.write(str(number) + '\n')
        writeExpo = open('biggestexponent.txt','w') # 'w' for write
        writeExpo.write(str(lim))
        writeExpo.close()

inpbits = input("How many bits would you like to save? ")
save_primes(inpbits)