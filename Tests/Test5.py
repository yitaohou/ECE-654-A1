#For testing if a nested structure with more or equal to 4 layers would trigger the detector
#Expected result: Fail
a = 1
b = 3
c = 8
if a < b:
    if b < c:
        if a == c:
            print ("not necessary step")
    else:
        if a == c:
            print ("not necessary step")
else:
    if b < c:
        for i in range(0,5):
            if i > 2:
                print ("yahooo!")
    else:
        print ("such a fool")