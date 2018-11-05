import math
import time

print ("Running!")
start = time.time()

# Generate the 22nd line of Pascal's Triangle
pascal = []
pascal.append([math.factorial(22)/(math.factorial(r) * math.factorial(22 - r))
            for r in range(0, 23)])
count = 0
# Generate subsequent lines by adding the two numbers "above"
# Check for numbers over a million on the way
for nTrue in range(23, 101):
    n = nTrue - 22
    pascal.append([])
    for r in range(0, len(pascal[n - 1]) + 1):
        if r == 0 or r == len(pascal[n - 1]):
            pascal[n].append(1)
        else:
            nextP = pascal[n - 1][r - 1] + pascal[n - 1][r]
            if nextP > 1000000:
                count += 1
            pascal[n].append(nextP)
                
end = time.time()
run = end - start
print ("%s found in %s seconds" % (count, "{0:.4f}".format(run)))