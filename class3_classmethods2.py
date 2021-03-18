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

	@classmethod
	def from_string(cls, emp_string):
		fname, lname, salary = emp_string.split(" ")
		return cls(fname, lname, salary)	

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True	
	


emp1 = Employee('Lionel', 'Messi', 10000)
emp2 = Employee('Cristiano', 'Ronaldo', 20000)


emp_string = 'Neymar Junior 8000'

emp3 = Employee.from_string(emp_string)

print(emp3.get_fullname())

import datetime
mydate = datetime.date(2021, 3, 12)
print(Employee.is_workday(mydate))


#Regular Methods pass (self) that is the instance of the class as the first paramater.

#Class Methods pass (cls) that is the class itself as the first paramater to the method.