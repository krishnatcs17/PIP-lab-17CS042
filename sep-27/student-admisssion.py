class Admission:
	def __init__(self):
		self.name = ''
		self.age = 0
		self.marks  = 0

	def set_data(self):
		self.name = input("Enter name: ")
		self.age = int(input("Enter age: "))
		self.marks = int(input("Enter marks: "))

	def validate_marks(self):
		if self.marks >= 0 and self.marks <= 100:
			return True
		print("Invalid marks")
		return False
	
	def validate_age(self):
		if self.age >= 20:
			return True
		print("Invalid age")
		return False

	def check_qualification(self):
		if self.validate_age() and self.validate_marks():
			if self.marks >= 65:
				return True
			print("Marks less than the qualifying marks")
			return False
		return False

	def get_data(self):
		print("For student - ", self.name)
		if self.check_qualification():
			print("Student is qualified")
			print("Name:", self.name)	
			print("Age:", self.age)
			print("Marks:", self.marks)
		else:
			print(self.name, "is not qualified", end='\n')




st = []
n = int(input("Enter the number of students: "))
for i in range(n):
	st.append(Admission())
	st[i].set_data()
	print()
print()
for j in range(n):
	st[j].get_data()
	print()



