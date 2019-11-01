import sqlite3 as sql

class EmployeeTable:
	def __init__(self):
		try:
			self.conn = sql.connect("company.db")
		except:
			print("Prblem with database connection! ")
		self.cursor = self.conn.cursor()
		self.cursor.execute("""create table if not exists employees (name varchar(20), emp_id varchar(4), salary int(6));""")

	def insertion(self):
		print("Enter the details of the employee ")
		name = input("Name : ")
		emp_id = input("Employee id : ")
		salary = int(input("Salary (only int) : "))
		self.cursor.execute('insert into employees values(?,?,?);', (name, emp_id, salary,))
		self.conn.commit()
	
	def displayAll(self):
		print("Info of all the employees ")
		print("Name".ljust(20)+"Employee ID".ljust(20)+"Salary".ljust(7))
		self.conn.row_factory = sql.Row
		self.cursor.execute("select * from employees;")
		rows = self.cursor.fetchall()
		for row in rows:
			print(row[0].ljust(20)+row[1].ljust(20)+str(row[2]).ljust(7))
		
	def deleteParticular(self):
		emp_id = input("Enter the employee id: ")
		try:
			self.cursor.execute("delete from employees where emp_id = '%s';" %(emp_id))
			print("Details of the employee with emp_id " + emp_id + " are deleted")
		except Exception as e:
			print("Employee data doesn't exist.", e)
		self.conn.commit()

	def displayParticular(self):
		emp_id = input("Enter the employee id: ")
		self.cursor.execute("select * from employees where emp_id = '%s';" %(emp_id))
		rows = self.cursor.fetchall()
		for row in rows:
			print("Name : "+row[0]+"\nEmp ID : "+row[1]+"\nSalary : "+str(row[2]))
		self.conn.commit()

	def updateInfo(self):
		emp_id = input("Enter the employee id: ")
		name = input("Enter the name ")
		salary = int(input("Enter the salary "))
		self.cursor.execute("update employees set name = '%s', salary = %d where emp_id = '%s' ;" %(name, salary, emp_id))
		print("Updated")
		self.conn.commit()
		

if __name__ == "__main__":
	emp = EmployeeTable()
	ch = 1
	print("Enter the option\n1.Insert\n2.Display\n3.Delete an employee\n4.Display an employee\n5.Update an employee\n0.Exit")
	while ch:
		ch = int(input("\nChoice: "))
		if ch == 1:
			emp.insertion()
		elif ch == 2:
			emp.displayAll()
		elif ch == 3:
			emp.deleteParticular()
		elif ch == 4:	
			emp.displayParticular()
		elif ch == 5:
			emp.updateInfo()
		else:
			print("Enter proper choice!")
	