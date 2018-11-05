# Naive solution, miserably slow at 2.97 s
# Checks a lot of numbers twice

largest = -1
for product in [a * b for a in range(100, 999) for b in range (100, 999)]:
    p = product
    digits = []
    match = True
    while p > 0:
        digit = p % 10
        digits.append(digit)
        p //= 10
    length = len(digits) // 2
    for d in range(0, length):
        if digits[d] != digits[-d - 1]:
            match = False
            break
    if match and product > largest:
        largest = product
        
#print (largest)
        