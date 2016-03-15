import math
g,b = [int(x) for x in raw_input().split()]
while g !=-1 and b !=-1:
	if g == b:
		if g == 0:
			print 0
		else:
			print 1
	else:
		x = max(g,b)
		y = min(g,b)
		if (x%(y+1)==0):
			print x//(y+1)
		else:
			print (x//(y+1)) + 1


	g,b = [int(x) for x in raw_input().split()]