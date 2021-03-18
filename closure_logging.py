import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):

	def log_func(*args):
		logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
		print(func(*args))

	return log_func



def add(x, y):
	return x + y

def substract(x, y):
	return x - y

add_logger = logger(add)
sub_logger = logger(substract)


add_logger(10, 5)
add_logger(10, 20)

sub_logger(3, 2)
sub_logger(7, 2)
