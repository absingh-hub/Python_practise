def shout(text):
	return text.upper()


def whisper(text):
	return text.lower()


def calling_fun(func):

	x = func('This is some Random Text')
	print(x)


calling_fun(shout)
calling_fun(whisper)
