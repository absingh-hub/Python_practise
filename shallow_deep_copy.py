original_list = [10, 20, 30, 40, 50]

shallow_copy_list = original_list

print(id(original_list[0]))
print(id(original_list[1]))
print(id(original_list[2]))
print(id(original_list[3]))

# print(shallow_copy_list)
print('Original--------------------------')

print(id(shallow_copy_list[0]))
print(id(shallow_copy_list[1]))
print(id(shallow_copy_list[2]))
print(id(shallow_copy_list[3]))

print('Shallow--------------------------')

import copy

deep_copy_list = copy.deepcopy(original_list)

print(id(deep_copy_list[0]))
print(id(deep_copy_list[1]))
print(id(deep_copy_list[2]))
print(id(deep_copy_list[3]))

original_list[0] = 20



print(deep_copy_list)
print(shallow_copy_list)


if original_list
  