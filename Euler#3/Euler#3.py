# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Based on prime boostrapping
# This is about 10 times slower, at 133 ms

number = 600851475143
numberCopy = number

primes = [2]
factors = []
p = 3  # type: int

while numberCopy > 1:
    isPrime = True
    maxIndex = primes.count(primes) - 1
    for i in range(0, maxIndex):
        if p % i == 0:
            primes = False
            break
    if isPrime:
        primes.append(p)
    while numberCopy % p == 0:
        factors.append(p)
        numberCopy /= p
    p += 2

print (factors[-1])