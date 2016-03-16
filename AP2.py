#spoj solutions
t = int(raw_input())
for i in range(t):

	third_term,third_last_term,s = [int(x) for x in raw_input().split()]
	n = 2*s/(third_term + third_last_term)
	d = (third_last_term - third_term)/(n-6)
	print str(n)
	a1 = (third_term - 2 *d)
	res = ''
	for k in range(n):
		term = a1 + k*d
		res = res + str(term) + ' '
	print res[:len(res)-1]