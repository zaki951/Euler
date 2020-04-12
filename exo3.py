#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


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

if __name__ == "__main__":

    n = 11**42
    i = int(n**0.5)
    while i > 1:
        if n % i == 0:
            if IsPrime(i) :
                break
        i-= 1
    print(i)

    """
    for i in range(200):
        if IsPrime(i) :
            print(i,end = " ")
    """