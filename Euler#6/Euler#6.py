sumofsquares = sum([x ** 2 for x in range(1, 101)], 0)
squareofsum = sum([x for x in range(1, 101)], 0) ** 2
difference = squareofsum - sumofsquares

#print (difference)