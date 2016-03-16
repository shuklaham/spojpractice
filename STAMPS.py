#spoj solutions
t = int(raw_input())
for i in range(t):
	flag = False
	deficit,numfriends = [int(x) for x in raw_input().split()]
	listofstamps = [int(x) for x in raw_input().split()]
	listofstamps.sort(reverse= True)
	s = 0
	for j in range(len(listofstamps)):
		s = s + listofstamps[j]
		if s >= deficit:
			flag = True
			need = j+1
			break
	if flag:
		print 'Scenario '+'#'+str(i+1)+':'
		print need
	else:
		print 'Scenario '+'#'+str(i+1)+':'
		print 'impossible'

