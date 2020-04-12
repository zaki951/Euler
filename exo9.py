"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math

def pythagorean (n):
    for a in range(1,int(n/2)):
        for b in range(1,int(n/2)):
            for c in range(1,int(n/2)):
                if a + b == n - c :
                    if a**2 + b**2 == c**2 :
                        return a,b,c
    return 0

print(pythagorean(1000))