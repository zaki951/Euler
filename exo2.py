#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""
def Fibonacci(n):
    fib = 0
    if (n <= 0 ):
        return 0
    elif (n == 1):
        return 1
    elif (n == 2):
        return 2
    else :
        fib += Fibonacci(n -1 ) + Fibonacci(n - 2)
    return fib
"""
def Fibonacci(n):
    if (n <= 0 ):
        return 0
    elif (n == 1):
        return 1
    elif (n == 2):
        return 1
    else :
        fib = 2
        a = 1
        b = 1
        for i in range(2 , n):
            fib = a + b 
            a = b
            b = fib
        return fib
        
def IsEven(n):
    if (n%2==0):
        return True
    else:
        return False 

if __name__ == "__main__":
    i = 0
    n = 0
    s = 0
    
    while(n < 4000000) :
        n = Fibonacci(i)
        if IsEven(n) :
            s += n
        i+= 1
    print(s)
    
