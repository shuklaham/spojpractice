
#from pprint import pprint

def minpath(inp):
	for row in range(N-2,-1,-1):
		for col in range(1,M+1):
			inp[row][col] = inp[row][col] + min(inp[row+1][col-1],inp[row+1][col],inp[row+1][col+1])
#pprint(inp)


N,M = map(int,raw_input().split())
inp = []
for i in range(N):
	city = [102] + map(int,raw_input().split()) + [102]
	inp.append(city)
if M==1:
	s = 0
	for i in range(N):
		s = s + inp[i][1]
	print s 
else:
	minpath(inp)
	print min(inp[0])
#pprint(inp)



