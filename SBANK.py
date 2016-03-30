#from collections import OrderedDict
#from pprint import pprint

tc = int(raw_input())
for i in range(tc):
	num = int(raw_input())
	l = []
	d = {}
	p = {}
	for _ in range(num):
		st = raw_input()
		s = st.strip()
		#s = st.split()
		#print len(s)
		#raw_input()
		#acc = int(s[0]+s[2]+s[3]+s[4]+s[5])
		#print acc
		#raw_input()
		#if st not in p:
		#	p[acc] = st
		if s not in d:
			d[s] = 1
		else:
			d[s] += 1

	#bank = str(s[1])
	#newD = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
	#pprint(p)
	#pprint(newD)
	l = d.keys()
	l.sort()
	for j in range(len(l)):
		#key_string = str(key)
		#raw_input()
		print l[j] +' '+ str(d[l[j]])
		#if j <= tc -2:
		#	print ''
		#raw_input()
	if i <=tc-2:
		print ''
		raw_input()