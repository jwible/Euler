def checkprime (y):
    check=3
    while check < y:
        if y % check ==0:
            break
        check=check+1
    if check == y:
        factors.append (y)

factors= [2,3]
a=5

while len(factors)<=10001:
    checkprime (a)
    a=a+2
    checkprime (a)
    a=a+4

print ("%d" % factors[10000])
