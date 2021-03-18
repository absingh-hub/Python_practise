def decorated_function(original_func):

	def wrapper_function(*args,**kwargs):
		print('this code is executed before {}()'.format(original_func.__name__))
		return original_func(*args,**kwargs)

	return wrapper_function

@decorated_function
def display():
	print("display function ran")

@decorated_function
def display_info(name, age):
	print("Hello my name is {} and age is {}".format(name,age))

display()
display_info('john',25)
