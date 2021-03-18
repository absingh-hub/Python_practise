# my_list = [1, 2, 3, 4, 5]

# try:
# 	print(my_list.index(3,3))

# except ValueError:

# 	print("Inside Value Error")	

#-----------------------------------------------

# my_list = [1, 2, 3, 4, 5]

# my_list.extend([6])

# print(my_list.extend([7]))
# print(my_list)


#-----------------------------------------------


# my_set = {1, 2, 3, 4, 5, 1, 2, 6}

# my_tuple = (1, 2, 3, 4, 5, 1, 2, 6)

# print(my_set)
# print(my_tuple)

#-----------------------------------------------


# my_list = [10, 20, 30, 40, 50]
# my_list.insert(2, 70)

# print(my_list)

# my_list.insert(len(my_list), 90)
# print(my_list)


#-----------------------------------------------


# my_list = [10, 20, 30, 40, 50]

# my_list.remove(30)
# print(my_list)

# try:
# 	my_list.remove(10)
# 	print("element is removed")
# except ValueError:
# 	print("Element Not Present")
	
#-----------------------------------------------
	

# my_list = ['aa', 'bb', 'cc', 'dd', 'aa', 'aa', 'cc']

# my_list = set(my_list)

# print(my_list)


#--------------------------------------------

# my_list = ['aa', 'bb', 'cc', 'dd', 'aa', 'aa', 'cc']

# # popped_ele = my_list.pop(0)

# my_list.remove('aa')

# print(my_list)


#--------------------------------------------

my_list = [1, 5, 3, 6, 2, 7]

# my_list.sort()
my_list.sort(reverse=True)

print(my_list)

asc_lis = sorted(my_list)
des_lis = sorted(my_list,reverse=True)
print('sorted List ', asc_lis)
print(des_lis)