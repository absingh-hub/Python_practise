# nums = [1, 2, 3]
# print(dir(nums))

#__iter__ is a dunder method or special method.
#if an object has __iter__ method that means it can be looped over and is an iterable.
#list is not a iterator as it doesnt have a state and doesnt have __next__ method



# print(next(nums))
#TypeError: 'list' object is not an iterator.
#in background it tried to run __next__ method but as list doest has this method it isnt 
#an iterator 


nums = [1, 2, 3]

# i_nums = nums.__iter__()  instead of calling dunder __iter__() like this we should 
#use iter() recommended in bakckground it calls same __iter__ method.

# print(i_nums)
# print(dir(i_nums))


i_nums = iter(nums)

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
# print(next(i_nums)) #error StopIteration exception


#iterators are an object with a state ie it remembers the its value at each next.
