class Employee:

	raise_percent = 1.5

	def __init__(self, fname, lname, salary):
		self.fname = fname
		self.lname = lname
		self.salary = salary
		
	@property	
	def email(self):
		return '{}.{}@gmail.com'.format(self.fname,self.lname)	

	@property
	def fullname(self):
		return '{} {}'.format(self.fname, self.lname)

	@fullname.setter
	def fullname(self, name):
		fname, lname = name.split(" ")
		self.fname, self.lname = fname, lname
		
	@fullname.deleter
	def fullname(self):
		print("Delete is working")
		self.fname = None
		self.lname = None	

	def apply_raise(self):
		self.salary = int(self.salary * self.raise_percent)



	def __repr__(self):
		return 'Repr-->Name {} {}'.format(self.fname, self.lname)
		
	def __str__(self):
		return 'Str-->Name {}'.format(self.fullname)

	def __add__(self, other):
		return self.salary + other.salary	

emp1 = Employee('Abhishek', 'Singh' , 100000)
emp2 = Employee('Akash', 'Purwar', 100000)


emp1.fullname = 'Chetan Tingase'

print(emp1)
print(emp1.email)
print(emp1.fullname)


del emp1.fullname
print(emp1)