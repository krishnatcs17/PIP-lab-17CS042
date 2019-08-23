def rev(arr):
	arr.reverse()
	print(*arr, end='\n')
	for i in range(len(arr)):
		arr[i] = arr[i][::-1]
	return arr


sent = input('Enter a long string: ')
arr = list(sent.split())

print(*rev(arr), end='\n')
