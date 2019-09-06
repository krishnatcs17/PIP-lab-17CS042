for num in range(1, 51):
	if num%3 == 0 and num %5 == 0:
		print('FizzBuzz', end=' ')
	elif num%3 == 0 and num%5:
		print('Fizz', end=' ')
	elif num%5 == 0 and num%3:
		print('Buzz', end=' ')
	else:
		print(num, end=' ')
print()
