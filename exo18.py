s = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

s = s.replace("\n","",1)
def toStringList(string):
    l = []
    s = ""
    for c in string :
        if c != '\n':
            s += c
        else :
            l.append(s)
            s = ""
    l.append(s)
    return l
def toIntList(l):
    newList = []
    l_temp = []
    nb = ""
    for s in l :
        for  c in s :
            if c != " ":
                nb += c
            else :
                l_temp.append(int(nb))
                nb = ""
        l_temp.append(int(nb))        
        nb = ""
        newList.append(l_temp.copy())
        l_temp.clear()
    #reconfig(newList)
    return newList

def reconfig(l):
    size = len(l[-1])
    for lnb in l :
        while(len(lnb) < size):
            lnb.append(0)
def add(*kwargs):
    for l in kwargs:
        l.append(0)

def exo18(triangle):
    maxi = 0
    somme1 = 0  
    somme2 = 0
    for i in reversed(range(0 , len(triangle))):
        for j in range(len(triangle[i])):
            if i - 1 >= 0 and j < len(triangle[i - 1]):
                somme1 = triangle[i][j] + triangle[i - 1][j]
            if i - 1 >= 0 and j + 1 < len(triangle[i]):
                somme2 = triangle[i][j + 1] + triangle[i - 1][j]
        
            maxi = max(somme1,somme2)
            if i - 1 >= 0 and j < len(triangle[i - 1]):
                triangle[i - 1][j] = maxi
            
    #return sumn , suml , sumr    
    return triangle[0][-1]
    
if __name__ == "__main__":
    l = toStringList(s)
    l = toIntList(l)
    print(exo18(l))