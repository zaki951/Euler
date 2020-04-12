def Fill100(): 
    l = []
    for i in range(101):
        l.append(i)
    return l

def SumOfSquare(l):
    s = 0
    for i in range(len(l)):
        l[i] = l[i]**2
    s = sum(l)
    return s
def SquareOfTheSum(l):
    s = 0
    for i in l:
        s += i
    s = s**2
    return s

prime = Fill100()
s1 = SquareOfTheSum(prime)

s2 = SumOfSquare(prime)
print(s1 - s2)
