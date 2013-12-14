"""Find the sum of all the primes below two million."""

limit = 2000000
a = int (limit/6)  #checking primes at 6k+/- 1 so going to stop when limit/6 issue if limit or limit+1 is divisible by 6
k=1


def divideByAllPrimes (x):
    for prime in primes:
        if x % prime == 0:
                return (False)
        if prime**2 > x:
            return (True)


while k != a+1:
    b =  k*6-1
    c =  k*6+1
    if divideByAllPrimes (b) == True:
        primes.append (b)
    if divideByAllPrimes (c) == True:
        primes.append (c)
    k=k+1


print (sum(primes))
    
"""EXPLANATION OF METHODOLOGY:

I combined methodologies. So let me explain them. I’ve seen others use them but never with an explanation.

1.	Only test numbers that are 6k+/-1:
All primes > 3 are expressible as 6k +/- 1. I’ve seen this in forums here but never with an explanation. Did some research and it’s true, definitively. Why?  Because 6k is divisible by 2 or 3; because 6 is. 6k +/- 2 is divisible by 2 obviously. 6k +/- 3  is divisible by 3. And you’re already encountering overlap (9 is expressible as 6*1+3 and 6*2-3), so you don’t need to test 4 or 5. That leaves 6k + or – 1. So I only tested numbers that fit this pattern. 

2.	Test By Dividing By Primes:
For each number I found that was prime I added it to a list. If a number is divisible by a prime it is not prime obviously. But you don’t need to divide by composite numbers (non-primes) as well because all composite numbers are all divisible by some smaller prime. The product of a composite any number is divisible by the prime the composite is. This is factorization for those who don’t remember their high school math.

3.	Stop dividing By Primes when greater than square root of number testing:
As I was adding them to the list in order when testing I started at the low end of the list and worked my way up. When the prime squared was greater than the number testing I stopped. There could be no number greater than that without being a corresponding number lesser than it. And I already tested everything lower than it, so it’s prime!
"""
