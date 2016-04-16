def getMinDist(pos,numCows):
	pos.sort()
	start = pos[0]
	end = pos[-1]
	while start < end:
		mid = start + (end - start + 1)//2
		if p(pos,numCows,mid):
			start = mid
		else:
			end = mid - 1
	return end


# numCows = 3
# pos = 1 2 4 8 9
# distance = 2
def p(pos,numCows,distance):
	numCows = numCows - 1
	prevPos = pos[0]
	done = False
	for i in xrange(1,len(pos)):
		if pos[i] - prevPos >= distance:
			numCows = numCows - 1
			if numCows == 0:
				done = True
				break
			prevPos = pos[i]
	return done	

tc = int(raw_input())
for i in xrange(tc):
	N,C = map(int,raw_input().split())
	pos = []	
	for i in xrange(N):
		pos.append(int(raw_input()))
	print getMinDist(pos,C)
		
