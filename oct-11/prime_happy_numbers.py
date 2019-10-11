p = open("happyNum.txt", 'r')
h = open("primeNum.txt", 'r')

pl = p.read()
plist = pl.split(', ')
hl = h.read()
hlist = hl.split(', ')

for i in range(min(len(plist), len(hlist))):
	if plist[i] == hlist[i]:
		print(plist[i], end=' ')

p.close()
h.close()
