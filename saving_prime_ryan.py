readf = open('primtal.txt')
appf = open('primtal.txt','a')

def save_primes(lim):
    for number in range(2,lim):
        if number not in readf:
            for line in readf:
                if number % int(line) == 0:
                    appf.write(str(number) + '\n')
                    break


save_primes(20)