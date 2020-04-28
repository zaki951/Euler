def decToBinaryStr(nb , size):
	s = (str(bin(nb)))[2:]

	while len(s) < size :
		s = "0"+ s
	return s

size = 6 * 2

def test(size):
	cpt = 0
	nb1 = 0
	nb0 = 0
	for i in range(2**int(size/2) - 1,2**size , 2) : 
		s = decToBinaryStr(i , size)
		nb1 = s.count("1")
		nb0 = s.count("0")
		if nb0 == nb1  :
			cpt += 1
		nb1 = 0
		nb0 = 0 
	return cpt * 2


for i in range(10):
    print(test(2 * i) , end = " ")




#print(len(newList))
