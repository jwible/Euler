def divideByAllPrimes (x,primes):
    for prime in primes:
        if x % prime == 0:
                return (False)
        if prime**2 > x:
            return (True)

def findPrimesLess(limit):
    a = int (limit/6)  #checking primes at 6k+/- 1 so going to stop when limit/6 issue if limit or limit+1 is divisible by 6
    primes = [2,3] #need to start with 2,3 because theyre the only ones not in the pattern 
    k=1
    
    
    while k != a+1:
        b =  k*6-1
        c =  k*6+1
        if divideByAllPrimes (b,primes) == True:
            primes.append (b)
        if divideByAllPrimes (c,primes) == True:
            primes.append (c)
        k=k+1
    return(primes)


primes = findPrimesLess(100000)
highestN = 0
solution = ()

for a in range  (-999, 1000, 1):
    for b in range (-999, 1000, 1):
        for n in range (0, 1000000):
            if ((n*n) + (n*a) + b)<0:
                break
            if divideByAllPrimes (((n*n) + (n*a) + b), primes) == True:
                if n > highestN:
                    highestN = n
                    solution = (a*b)
                    n=n+1
            else:
                break

print (solution)
