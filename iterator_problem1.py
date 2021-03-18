
class Sentence:

	def __init__(self, string):
		self.string = string
		self.current = 0


	def __iter__(self):
		return self

	def __next__(self):

		list_string = self.string.split()

		while True:

			if self.current < len(list_string):
				word = list_string[self.current]
				self.current += 1
				return word
			else:
				raise StopIteration
	

my_sentence = Sentence('Hello all hows u great')


# print(my_sentence)
# print(dir(my_sentence))

# for word in my_sentence:
# 	print(word)

print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))