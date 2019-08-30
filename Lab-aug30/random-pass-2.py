import random
import string
charLower = list(string.ascii_lowercase)
charUpper = list(string.ascii_uppercase)
charDigit = list(string.digits)
charPunct = list(string.punctuation)
random.shuffle(charLower); random.shuffle(charUpper); random.shuffle(charDigit); random.shuffle(charPunct)
password = ''
n = random.randint(10, 16)
for i in range(n):
	j = random.randint(0, 3)
	if j == 0:
		password += charLower[random.randint(0, len(charLower)-1)]
	if j == 1:
		password += charUpper[random.randint(0, len(charUpper)-1)]
	if j == 2:
		password += charDigit[random.randint(0, len(charDigit)-1)]
	if j == 3:
		password += charPunct[random.randint(0, len(charPunct)-1)]


print("Password: ", password)
