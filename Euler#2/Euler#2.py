# Fairly naive solution

fib = [1, 1]
i = 2
total = 0

while fib [-1] < 4000000:
    fib.append(fiball [i - 1] + fib [i - 2])
    if fib [i] % 2 == 0: total += fib [i]
    i += 1
    
print (total)