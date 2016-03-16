#spoj solutions
def canton(number):
	if(number == 1):
		print "TERM 1 IS 1/1"
		return None
	else:
		i = 1
		n = 1
		while n < number:
			i = i + 1
			n = n + i
		nmin = n - i + 1
		nmax = n
		if i % 2 == 0:
			num = number - nmin + 1
			den = nmax - number + 1
		else:
			num = nmax - number + 1
			den = number - nmin + 1
		print "TERM "+str(number) + ' IS '+str(num)+'/'+str(den)
		return None

t = int(raw_input())
for k in range(t):
	canton(int(raw_input()))








