#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?


def IsPrime(n):
    if (n == 1):
        return False
    elif (n == 0):
        return False
    elif(n==2):
        return True
    elif (n%2 == 0):
        return False
    else :
        i = int(n**0.5)
        while (i > 1) :
            if n%i == 0:
                return False
            i -= 1
        return True


i = 0
nbPrime = 0
while(1):
    if(IsPrime(i)):
        nbPrime += 1
    if nbPrime >= 10001 :
        break
    i += 1

print(i)