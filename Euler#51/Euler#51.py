#By replacing the 1st digit of the 2-digit number *3, 
#it turns out that six of the nine possible values: 
#13, 23, 43, 53, 73, and 83, are all prime.
#
#By replacing the 3rd and 4th digits of 56**3 with the same digit, 
#this 5-digit number is the first example 
#having seven primes among the ten generated numbers, 
#yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
#Consequently 56003, being the first member of this family, 
#is the smallest prime with this property.
#
#Find the smallest prime which, by replacing part of the number 
#(not necessarily adjacent digits) with the same digit, 
#is part of an eight prime value family.

import time

print ("Running!")
start = time.time()

primes = [2]
for p in range(3, 1000000, 2):
    isPrime = True
    i = 0
    while primes[i] ** 2 <= p:
        if p % primes[i] == 0:
            isPrime = False
            break
        i += 1
    if isPrime:
        primes.append(p)
    
smallest = 0
for i in [x for x in range(0, len(primes)) if primes[x] > 100000]:
    prime = primes[i]
    for d in range(0, 3):
        primeCopy = prime
        iterator = 0
        digitIndex = 0
        matchCount = 0
        while primeCopy > 0:
            digit = int(primeCopy) % 10
            primeCopy = primeCopy // 10
            digitIndex += 1
            if digit == d and digitIndex > 0:
                iterator += 10 ** digitIndex
        if iterator == 0:
            continue
        primeCopy = prime
        while primes.count(primeCopy) == 1 and primeCopy < 1000000:
            matchCount += 1
            primeCopy += iterator
        if matchCount == 8:
            smallest = prime
            break
    if smallest > 0:
        break

end = time.time()
run = end - start
print ("%s found in %s seconds" % (smallest, "{0:.4f}".format(run)))