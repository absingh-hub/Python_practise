class decorator_class(object):

	def __init__(self, original_function):
		self.original_function = original_function

	def __call__(self, *args, **kwargs):		
		print('this code is executed before {}()'.format(self.original_function.__name__))
		return self.original_function(*args,**kwargs)

@decorator_class
def display():
	print("Display function is executed")


@decorator_class
def display_info(name, age):
	print("Hello my name is {} and age is {}".format(name,age))


display()
display_info("Mika" ,  22)