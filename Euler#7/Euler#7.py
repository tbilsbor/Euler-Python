primes = [2]
p = 3
while len(primes) < 10001:
    isPrime = True
    i = 0
    while primes[i] ** 2 <= p:
        if p % primes[i] == 0:
            isPrime = False
            break
        i += 1
    if isPrime:
        primes.append(p)
    p += 2

print(primes[10000])