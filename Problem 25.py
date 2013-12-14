"""What is the first term in the Fibonacci sequence to contain 1000 digits?
Fibonacci sequence is the sequence that starts 1,1 - all subsequent are sum of
two prior. So 1,1,2,3,5,8..."""

import time
start_time = time.time()
f1 = 0
f2= 1
sequence = 1


while True:
    f3 = f1+f2
    f1 = f2
    f2 = f3
    sequence += 1
    if len (str (f2))>999:
        break

print (sequence)
print (time.time() - start_time, "seconds" )   
