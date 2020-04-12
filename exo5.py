def isDisible(n):
    for i in range(1,20):
        if (n % i != 0) :
            return False
    return True


i = 20
while(1):
    if isDisible(i):
        break
    i+= 1

print(i)
