"""Find the sum of all the positive integers which cannot be written
as the sum of two abundant numbers. An Abundant number is a number
where the sum of the natural divisors are greater than the number itself. """

import time
start_time = time.time()
limit = 28123 #all numbers over this can be expressed as the sum of two abundants

def findAbundants (z):
    abundants = []
    for x in range (z):
        a=0
        for y in range (2, int(x**.5)+1):
            if x%y == 0:
                if y*y == x:
                    a += y
                else:
                    a += y + int (x/y)
            if a > x:
                abundants.append (x)
                break
    return (abundants)

def sumtwoAbundants (abundants):
    #using itertools 
    sumoftwo = []
    for x in range (len(abundants)-1):
        first = abundants [x]
        for y in range (x,len(abundants)-1) :
            second = abundants [y]
            sumoftwo.append (first + second)
            if first+second > limit:
                break
    return (list(set (sumoftwo)))

sumoftwo= sumtwoAbundants (findAbundants(limit)) #find abundants finds all of them, then the sum sums the list of them
answer = 0
y=0
for x in range (1,limit): #because the summed abundants are in order checking all numbers till I hit next in list
    if x == sumoftwo [y]: 
       y += 1 #....then moving to next item in list
    else:
        answer += x


print (answer)
print (time.time() - start_time, "seconds" )   
