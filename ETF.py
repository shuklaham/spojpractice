import math

def etf(num):
	actualnum = num
	flag = False
	result = 1.0	
	while(num%2==0):
		flag = True
		num = num/2
	if flag:
		result = result * (1.0 - 1.0/float(2))
	for i in range(3,int(math.ceil(math.sqrt(num))),2):
		if num % i:
			result = result * (1.0 - 1.0/float(i))

		num = num/i
	if num > 2:
		result = result * (1.0 - 1.0/float(num))
	
	result = result * actualnum
	return result 

tc = int(raw_input())
for i in range(tc):
	num = int(raw_input())
	print int(etf(num))
