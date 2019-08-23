arr = list(map(int, input("Enter numbers in ascending order: ").split()))
n = int(input('Enter the number: '))


def search(a, n):
  return n in a
  
 
if(search(arr, n)):
  print(n, " is present")
else:
  print(n, " is not present")
