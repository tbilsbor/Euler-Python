# Already super fast, runs in 13.1 ms

# Start with the primes
s = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
# 4
s *= 2
# 6 is already covered by 2 * 3
# 8
s *= 2
# 9 
s *= 3
# 10 = 2 * 5, covered
# 12 = 2 * 2 * 3, covered
# 14 = 2 * 7, covered
# 15 = 3 * 5, covered
# 16
s *= 2
# 18 = 9 * 2, covered
# 20 = 2 * 2 * 5, covered

#print(s)