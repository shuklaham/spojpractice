#spoj solutions
perm_num = int(raw_input())
while perm_num:
	flag = True
	a = [int(x) for x in raw_input().split()]
	t = []
	for i in range(len(a)):
		num = a[i]
		if a[num-1] != i+1:
			flag = False
			break
	if flag:
		print 'ambiguous'
	else:
		print 'not ambiguous'
	perm_num = int(raw_input())
