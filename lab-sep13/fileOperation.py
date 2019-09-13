f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")

f1content = f1.read().split()
f2content = f2.read().split()

i = 0
j = 0
opList = []
while i < len(f1content) and j < len(f2content):
	len1 = (len(f1content[i])+1)//2 
	len2 = (len(f2content[j]) + 1)//2
	
	opList.append(f1content[i][:len1] + f2content[j][:len2])
	i += 1
	j += 1

while i < len(f1content):
	len1 = (len(f1content[i]) +1)//2

	opList.append(f1content[i][:len1])
	i += 1

while j < len(f2content):
	len2 = (len(f2content[j])+1) // 2
	
	opList.append(f2content[j][:len2])
	j += 1

with open("outputfile.txt", "w") as f:
	f.write(' '.join(opList))





