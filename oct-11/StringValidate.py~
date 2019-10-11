class StringValidate:
	def __init__(self, strInput):
		self.strInput = strInput
		self.li	= {')':'(', ']':'[', '}':'{'}	

	def validate(self):
		stk = []
		for ch in self.strInput:
			if ch in self.li.values():
				stk.append(ch)
			elif ch in self.li.keys():
				if len(stk) == 0:
					return False
				if stk[-1] == self.li[ch]:
					stk.pop()
		if len(stk) == 0:
			return True
		return False


inpString = input("Enter input string: ")
ob = StringValidate(inpString)
if ob.validate():
	print("Balanced string")
else:
	print("Imbalanced string")
							
				
		
