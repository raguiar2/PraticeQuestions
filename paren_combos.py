
paren_set = set()
def print_parens(n,paren_str):
	global paren_set
	if n == 0:
		return paren_str
	paren_set.add(print_parens(n-1,'('+paren_str+')' ))
	paren_set.add(print_parens(n-1, paren_str + '()'))
	paren_set.add(print_parens(n-1, '()'+paren_str))




n = int(input())



print_parens(n,'')


for elem in paren_set:
	if elem is not None:
		print(elem)