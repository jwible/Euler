
"""Find the sum of the digits in the number 100!"""

import math #standard library module

number = str(math.factorial (100))
sumofnumber = 0
for digits in number:
    digits = int(digits)
    sumofnumber += digits
print (sumofnumber)
