arr = list(map(int, input("Enter numbers in ascending order: ").split()))
n = int(input('Enter the number: '))


def search(a, n):
  return n in a
  
 
print(search(arr, n))

