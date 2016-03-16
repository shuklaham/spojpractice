#spoj solutions
t = int(raw_input())
for i in range(t):
	space = raw_input()
	num_NG,num_NM = [int(p) for p in raw_input().split()]
	NG = [int(x) for x in raw_input().split()]
	NM = [int(y) for y in raw_input().split()]
	
	'''dict_ng = dict()
	for i in range(len(NG)):
		if NG[i] not in dict_ng:
			dict_ng[NG[i]] = 1
		else:
			dict_ng[NG[i]]=+1

	dict_nm = dict()
	for i in range(len(NM)):
		if NM[i] not in dict_nm:
			dict_nm[NM[i]] = 1
		else:
			dict_nm[NM[i]]= +1
	#print dict_ng.keys()
	#print dict_nm.keys()

	ng_power = dict_ng.keys()
	ng_power.sort()
	nm_power = dict_nm.keys()
	nm_power.sort()'''

	ng_power_max = max(NG)
	nm_power_max = max(NM)

	if ng_power_max > nm_power_max:
		print 'Godzilla'
		continue
	elif ng_power_max < nm_power_max:
		print 'MechaGodzilla'
	else:
		print 'Godzilla'
