#spoj solutions
T = raw_input()
total_input = int(T)
for i in xrange(total_input):
	num = int(raw_input())
	count = 0
	while(num>=5):
		count=count+num/5
		num=num/5
	print count
	