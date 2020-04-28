def numberToStr(nb):
    numbers = ["","one","two","three","four","five","six","seven","eight","nine","ten",
                "eleven"," twelve","thirteen","fourteen","fifteen","sixteen","seventeen",
                "eighteen", "nineteen","twenty","thirty","forty","fifty","sixty","seventy",
                "eighty","ninety"]

    if nb == 0 :
        return "zero"
    nbDigits = len(str(nb))
    if nb <= 20 :
        return numbers[nb]
    elif nbDigits == 2 :
        s = numbers[20 + int(str(nb)[0]) - 2] + " "
        s += numbers[int(str(nb)[1])]
        return s
    elif nbDigits == 3 :
        s = numbers[int(str(nb)[0])]
        s += " hundred"
        if int(str(nb)[1]) == 0 and int(str(nb)[2]) == 0 :
            return s
        s += " and"
        if int(str(nb)[1] + str(nb)[2]) <= 20 :
            s+= " " + numbers[int(str(nb)[1] + str(nb)[2])]
        else :
            s += " " + numbers[20 + int(str(nb)[1]) - 2] 
            if int(str(nb)[2]) != 0 :
                s += " " + numbers[int(str(nb)[2])]
        return s
    elif nb == 1000 :
        return "one thousand"
    else :
        return "not now"

s = ""
for i in range(1,1001):
    s += numberToStr(i)
    #print(numberToStr(i))

s = s.replace(" ","")
print(len(s))

