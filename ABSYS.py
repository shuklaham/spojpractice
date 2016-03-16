#spoj solutions
def gimme_string(expr):	
	operand1,operand2 = expr.split(' + ')
	operand2,operand3 = operand2.split(' = ')
	'''print operand1
	print operand2
	print operand3'''
	if 'm' in operand1 or 'a' in operand1 or 'c' in operand1 or 'h' in operand1 or 'u' in operand1 or 'l' in operand1 or 'a' in operand1:
		return str(int(operand3) - int(operand2)) + ' + ' + operand2 + ' = ' + operand3
	elif 'm' in operand2 or 'a' in operand2 or 'c' in operand2 or 'h' in operand2 or 'u' in operand2 or 'l' in operand2 or 'a' in operand2:
		return operand1 + ' + ' + str(int(operand3) - int(operand1)) + ' = ' + operand3
	else:
		return operand1 + ' + ' + operand2 + ' = ' + str(int(operand1) + int(operand2))

t = int(raw_input())
for i in range(t):
	e = raw_input()
	print gimme_string(e)

