class Employee:

	raise_amount = 1.2

	def __init__(self, fname, lname, salary):
		self.fname = fname
		self.lname = lname
		self.salary = salary


	def get_fullname(self):
		return '{} {}'.format(self.fname, self.lname)


	def apply_raise(self):
		self.salary = int(self.salary * self.raise_amount)

	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount



emp1 = Employee('Lionel', 'Messi', 10000)
emp2 = Employee('Cristiano', 'Ronaldo', 20000)

# print(emp1.get_fullname())
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

Employee.set_raise_amount(1.5)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

