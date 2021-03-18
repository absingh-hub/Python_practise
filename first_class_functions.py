def html_tag(tag):

	def wrap_text(msg):
		print('<{0}>{1}</{0}>'.format(tag, msg))
		
	return wrap_text
	

print_h1 = html_tag('h1')
# print(print_h1)

print_h1("First Content")
print_h1("Second Content")


print_div = html_tag('div')
print_div("First Div")
print_div("Second Div")