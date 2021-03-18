class Employee:

	raise_percent = 1.5

	def __init__(self, fname, lname, salary):
		self.fname = fname
		self.lname = lname
		self.salary = salary
		

	def get_fullname(self):
		return '{} {}'.format(self.fname, self.lname)

	def apply_raise(self):
		self.salary = int(self.salary * self.raise_percent)

emp1 = Employee('Abhishek', 'Singh' , 100000)
emp2 = Employee('Akash', 'Purwar', 219312)

# print(emp1.get_fullname())
# print(emp2.get_fullname())

# print(Employee.get_fullname(emp1))


print(emp1.salary)
emp1.apply_raise()
print(emp1.salary)