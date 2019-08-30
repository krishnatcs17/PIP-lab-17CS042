import random
import string
charList = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
chars = []
for i in charList:
	chars.append(i)
random.shuffle(chars)
password = ''
n = int(input("Enter the password length: "))
for j in range(n):
	password += chars[random.randint(0,len(charList))]
print("Password: ", password)
