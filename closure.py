def outer_function():
	name = 'Abhishek'

	def inner_function():
		print(name)

	return inner_function


my_func = outer_function()
print(my_func.__name__)

my_func()


#Closures is a inner function that remembers has access to variables of outer functions 
#even after the outer function has finished executing