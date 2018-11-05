import time

print ("Running!")
start = time.time()

smallest = -1
mag = 100
n = 11
while (smallest < 0):
    if n > mag // 3:
        n = mag + 1
        mag *= 10
        continue
    nCopy = n
    nDigits = []
    match = True
    while nCopy > 0:
        digit = nCopy % 10
        nDigits.append(digit)
        nCopy //= 10
    for m in range (2, 7):
        nCopy = n * m
        mDigits = []
        while nCopy > 0:
            digit = nCopy % 10
            mDigits.append(digit)
            nCopy //= 10
        nDigits.sort()
        mDigits.sort()
        if nDigits != mDigits:
            match = False
            break
    if match:
        smallest = n
        break
    n += 1
        
end = time.time()
run = end - start
print ("%s found in %s seconds" % (smallest, "{0:.4f}".format(run)))
        
    