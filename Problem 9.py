answer = []
c = 650
b = 999 - c
"""largest c corresponds to triplet 997,2,1, largest b must assume a = 1 so 1000 - c - 1 or 999 - c"""


def check_all_b_a (c):
    b = 999 - c
    a = 1
    while b> a:
        if (a*a + b*b) == (c*c):
            answer.append (a*b*c)
            print ('found it')
            print (a, b, c)
            return True
        b=b-1
        a=a+1

while c>335:
    if check_all_b_a(c) == True:
        print (answer)
        break
    c=c-1
    b = 999 - c
