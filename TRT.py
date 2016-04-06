#see quora for hint, recieving TLE

def trt(be,en):
	#print 'Now be is -- > ' + str(be)
	#print 'Now en is -- > ' + str(en)
	global N
	global values
	global cache
	year = N - (en - be)
	if be > en:
		return 0
	if cache[be][en] != -1:
		return cache[be][en]
	cache[be][en] = max(trt(be+1,en) + year*values[be],trt(be,en-1)+ year*values[en])
	return cache[be][en] 
	


N = int(raw_input())
values = []
be = 0
en = N - 1
cache = [[-1 for x in range(N)]for y in range(N)]
for i in range(N):
	values.append(int(raw_input()))

trt(be,en)
print cache[0][N-1]
	

				
