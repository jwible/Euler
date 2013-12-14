"""What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

def Divisible_1_to_20 (x):
    for i in range (1,21,1):
        if x % i > 0:
            break
        if i == 20:
            smallest_number = x
            print ('ITS', smallest_number)
            return True

smallest_number = 0
x = 2520
while smallest_number == 0:
    if Divisible_1_to_20 (x) == True:
        break
    x=x+2520


