"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factIterrative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def factRecursive(n):
    if n <= 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return factRecursive(n - 1) * n

fact100 = str(factIterrative(100))
somme = 0
for i in fact100:
    somme += int(i)

print(somme)