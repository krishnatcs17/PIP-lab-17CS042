def printPattern(size):
	for _ in range(size):
		print(" ---" * (size - 1))
		print("|  " * size)
	print(" ---" * (size - 1))

n = int(input("Enter number of rows: "))
printPattern(n)
