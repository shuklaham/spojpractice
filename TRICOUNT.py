#spoj solutions
t = int(raw_input())
for i in range(t):
	n = int(raw_input())
	if n % 2 == 0:
		print n*(n+2)*(2*n+1)/8
	else:
		print (n*(n+2)*(2*n+1)-1)/8

