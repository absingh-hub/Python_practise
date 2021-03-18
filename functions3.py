def outer_function(x):
	def inner_function(y):
		return x + y
		
	return inner_function


adding_function = outer_function(10)

print(adding_function(20))