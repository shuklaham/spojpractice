#spoj solutions
import math 
while True:
	b,g = [int(x) for x in raw_input().split()]
	if	b ==-1 and g ==-1:
		break
	if b == g:
		if b == 0:
			print 0
		else:
			print 1
	else:
		x = max(b,g)
		y = min(b,g)
		print int(math.ceil(x / (y + 1)))
