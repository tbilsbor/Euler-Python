# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Just calculating factors without worrying about primes
# This is about ten times faster, at 13.9 ms

number = 600851475143
numberCopy = number

factors = []
p = 3  # type: int

while numberCopy > 1:
    while numberCopy % p == 0:
        factors.append(p)
        numberCopy /= p
    p += 2

print (factors[-1])