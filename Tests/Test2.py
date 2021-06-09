#For testing if a nested structure with less than 4 layers but present of if statement more than 4 times would trigger the error.
#Expected result: Pass
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
        print ("yahooo!")
    else:
        print ("such a fool")
