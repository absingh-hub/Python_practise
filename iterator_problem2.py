def generator_sentence(sentence):
	for word in sentence.split():
		yield word

my_sentence = generator_sentence("Hi guys how are you")

# for word in my_sentence:
# 	print(word)


print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))