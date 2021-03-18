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


	def __repr__(self):
		return 'Repr-->Name {} {}'.format(self.fname, self.lname)
		
	def __str__(self):
		return 'Str-->Name {}'.format(self.get_fullname())

	def __add__(self, other):
		return self.salary + other.salary	

emp1 = Employee('Abhishek', 'Singh' , 100000)
emp2 = Employee('Akash', 'Purwar', 100000)



# print(emp1)

# print(repr(emp1))


print(int.__add__(1, 1))
print(str.__add__('hel', 'lo'))

print(emp1 + emp2)