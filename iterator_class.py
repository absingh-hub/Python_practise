class MyRange:
	
	def __init__(self, start, end):
		self.value = start
		self.end = end

	def __iter__(self):
		return self

	def __next__(self):

		if self.value >= self.end:
			raise StopIteration

		current = self.value
		self.value += 1
		return current
		

nums = MyRange(1, 10)

print(nums)
print(dir(nums))

for num in nums:
	print(num)