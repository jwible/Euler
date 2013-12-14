""" What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""

import itertools #standard library module, does it in lexicographic order

y=0
for x in itertools.permutations (range (10)):
    y += 1
    if y == 1000000:
        print (x)
        break
