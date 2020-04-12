"""
def palindrome(n):
    millier = int (n/1000)
    centaine = int(n/100) - millier * 10
    dizaine = int(n/10) - (centaine * 10  + millier *100)
    unite =  n - (millier * 1000 + centaine * 100 + dizaine * 10)
    nouveauNombre = unite * 1000 + dizaine * 100 + centaine * 10 + millier
    print(unite)
    if (nouveauNombre == n) :
        return True
    else:
        return False
"""

import math


"""
def isPalindrome(n):
    if n>=10:
        digits = int(math.log10(n))+1
        if digits >= 2 :
            fact = 10**(digits-1)
            l = []
            l.append(int(n/fact))
            for i in range(1 , digits):
                fact = int(10**(digits - i ))
                l.append( int((n%fact)/ (10**(digits - i - 1 ))) )
            l1 = l.copy()
            l.reverse()
            if l1 == l :
                return True
            else :
                return False
        else :
            return False
    else :
        return False
"""
def isPalindrome(nb):
    if str(nb) == str(nb)[::-1]:
        return True
    return False

resultat = 0
n = 1
for i in range(999, -1, -1):
    for j in range(999, -1, -1):
        n = i * j
        if isPalindrome(n):
            if n > resultat :
                resultat = n
    
print(resultat)