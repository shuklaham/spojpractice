#spoj solutions
import math
l = int(raw_input())
while l != 0:
	area = l*l/(2*float(math.pi))
	print("%.2f" % area)
	l = int(raw_input())