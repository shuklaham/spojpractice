import math
tc = int(raw_input())
for i in range(tc):	
	a,b,c,d = map(float,raw_input().split())
	s = (a+b+c+d)/2.0
	area = math.sqrt((s-a)*(s-b)*(s-c)*(s-d))
	print area

