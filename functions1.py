def myFunc(text):
	return text.upper()

#In python functions are first class objects as they can be assigned to a variable
#the variable stores the referece of the function object assigned.
hello = myFunc

print(hello("this is some text"))


