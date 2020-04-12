def decToBinaryStr(nb , size):
	s = (str(bin(nb)))[2:]

	while len(s) < size :
		s = "0"+ s
	return s

size = 20 * 2

allNb = []
for i in range(0,2**size) : 
	allNb.append(decToBinaryStr(i , size))



newList = []
nb1 = 0
nb0 = 0
for s in allNb :
	for c in s :
		if c == '1' :
			nb1 += 1
		else:
			nb0 += 1
	if nb0 == nb1  :
		newList.append(s)
	nb1 = 0
	nb0 = 0 

print(len(newList))