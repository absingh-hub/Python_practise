# class Employee:

# 	raise_percent = 1.2

# 	def __init__(self, fname, lname, salary):
# 		self.fname = fname
# 		self.lname = lname
# 		self.email = fname + '_' + lname + '@gmail.com'
# 		self.salary = salary
		

# 	def get_fullname(self):
# 		return '{} {}'.format(self.fname, self.lname)

# 	def apply_raise(self):
# 		self.salary = int(self.salary * self.raise_percent)



# class Developer(Employee):

# 	raise_percent = 1.4
	
# 	def __init__(self, fname, lname, salary, prg_lang):
		
# 		super().__init__(fname, lname, salary)
# 		self.prg_lang = prg_lang



# dev1 = Developer('Lionel', 'Messi', 10000, 'Python')
# dev2 = Developer('Cristiano', 'Ronaldo', 20000, 'Java')

# # print(emp1.salary)
# # emp1.apply_raise()
# # print(emp1.salary)

# # print(dev1.prg_lang)
# # print(help(Developer))
# # print(emp1.email)
# # print(emp2.email)


# class Manager(Employee):

# 	def __init__(self, fname, lname, salary, employees=None):
		
# 		super().__init__(fname, lname, salary)
		
# 		if employees is None:
# 			self.employees = []

# 		else:
# 			self.employees = employees


# 	def add_employee(self, emp):
# 		if emp not in self.employees:
# 			self.employees.append(emp)

# 	def remove_employee(self, emp):
# 		if emp in self.employees:
# 			self.employees.remove(emp)

# 	def print_employees(self):
# 		for emp in self.employees:
# 			print('--->',emp.get_fullname())						




# manager_1 = Manager('Steve', 'Smith', 3500, [dev1])

# print(manager_1.email)

# manager_1.add_employee(dev2)
# manager_1.print_employees()

# manager_1.remove_employee(dev2)

# manager_1.print_employees()

def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(starts_with_A, fruit)

print(map_object)
print(list(map_object))