def decorated_function(original_func):

	def wrapper_function():
		print('this code is executed before {}()'.format(original_func.__name__))
		return original_func()

	return wrapper_function


def display():
	print("display function ran")


my_func = decorated_function(display)
my_func()

#Decorators are used add some funtionality to our original function without changing the 
#original function