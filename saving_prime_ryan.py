readfile = open('primtal.txt')

def in_file(numberino): # Decides if the number is in the file 'primtal.txt'
    readf = open('primtal.txt')
    readf.seek(0)
    for line in readf:
        if int(line) == numberino:
            return True


def save_primes(lim): # Saves primes in file 'primtal.txt' if number is prime and not in file already
    for number in range(2,lim):
        if in_file(number) != True:
            is_prime = True
            readfile.seek(0)
            for line in readfile:
                if number % int(line) == 0:
                    is_prime = False
                    break
            if is_prime:
                appendf = open('primtal.txt','a')
                appendf.write(str(number) + '\n')

save_primes(2**16)
readfile.seek(0)
readfile.read()