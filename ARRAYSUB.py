from collections import deque

size = int(raw_input())
inp = map(int,raw_input().split())
subsize = int(raw_input())
maxV = findMax(inp,0,subsize-1)
for i in range(subsize,size+1):
	if