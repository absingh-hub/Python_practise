nums = [1, 2, 3]


#for num in nums:
 # print(num)

#this for loop is equivalent to following working in background

i_num = iter(nums)

while True:
	try:
		num = next(i_num)
		print(num)

	except StopIteration:
		break
	
#Iterators can only go forward through __next__ method	