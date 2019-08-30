n = int(input("Enter a number: "))
div = []
for i in range(1, n//2+1):
	if n%i is 0:
		div.append(i)
print("List of divisors: ", div)
