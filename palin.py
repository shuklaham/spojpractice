#spoj solutions
'''def next_palin(num):
	st = str(num)
	if st[0:(len(st)/2):1] == st[-1:-(len(st)/2+1):-1]:
		return num
	next_num = next_palin(num+1)
	return next_num
'''

t = int(raw_input())
for i in range(t):
	num = raw_input()
	if num == '9'*len(num):
		print int(num)+2
		continue
	elif int(num) < 9:
		print 11
		continue
	left_mid = num[0:len(num)/2:1]
	right_mid = num[-1:-len(num)/2-1:1]
	if len(num)%2 == 0:
		new_num = left_mid+left_mid[::-1]
	else:
		new_num = left_mid + num[len(num)/2] + left_mid[::-1]
	if int(new_num) > int(num):
		print next_num
		continue
	else:
		if len(num)%2==0 and num[0] !='0':
			l = new_num[0:len(new_num)/2:1]
			l_new = str(int(l) +1)
			next_num = l_new + l_new[::-1]
			print next_num
			continue
		elif len(num)%2==0 and num[0] =='0':
			l = new_num[0:len(new_num)/2:1]
			l_new = '0'*(len(l)-len(str(int(l)+1)))+str(int(l)+1)
			next_num = l_new + l_new[::-1]
			print next_num
			continue
		elif len(num)%2!=0 and num[0] !='0':
			l = new_num[0:len(new_num)/2+1:1]
			l_new = str(int(l) +1)
			next_num = l_new[:len(l_new)-1] + l_new[::-1]
			print next_num
			continue
		elif len(num)%2 != 0 and num[0] !='0':
			l = new_num[0:len(new_num)/2+1:1]
			l_new = '0'*(len(l)-len(str(int(l)+1))) + str(int(l)+1)
			next_num = l_new[:len(l_new)-1] + l_new[::-1]
			print next_num
			continue










