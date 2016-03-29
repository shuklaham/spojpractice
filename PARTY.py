#getting TLE but passing all test cases
from pprint import pprint

def knapsack_problem(knapsack_weight,w,v):
	#print 'knapsack_weight ' + '{:d}'.format(knapsack_weight)
	#print 'items value ',
	#print v
	#print 'items_weight ',
	#print w 
	k = xrange(knapsack_weight+1)
	T = [[None for col in xrange(knapsack_weight+1)]for row in xrange(len(w))]
	for col in xrange(knapsack_weight+1):
		if k[col] >= w[0]:
			T[0][col] = v[0]
		else:
			T[0][col] = 0
	for row in xrange(len(w)):
		T[row][0] = 0

	for row in xrange(1,len(w)):
		for col in xrange(1, knapsack_weight+1):
			if k[col] >= w[row]:
				T[row][col] = max(T[row-1][col],v[row] + T[row-1][k[col]-w[row]])
			else:
				T[row][col] = T[row-1][col]

	#for row in range(len(T)):
		#print T[row]

	row = len(w)-1
	col = knapsack_weight
	items = []
	sum_weight = 0
	sum_val = 0
	while row >=0 and col >= 0:
		if row == 0:
			if sum_weight + w[row] < knapsack_weight:
				items.append((v[row],w[row]))
				sum_weight = sum_weight + w[row]
				sum_val = sum_val + v[row]
				#print str(w[row])
				break
		#print str(row) + ' ' + str(col)
		if T[row][col] == T[row-1][col]:
			row = row - 1
			continue
		else:
			if sum_weight + w[row] < knapsack_weight:
				items.append((v[row],w[row]))
				sum_weight = sum_weight + w[row]
				sum_val = sum_val + v[row]
				#print str(w[row])
				col = col - w[row]
				row = row -1

	if len(T) == 1 and all([ v == 0 for v in T[0]]):
		print str(0) +' '+ str(T[0][knapsack_weight])
	else:
		#for item in items:
		#	print 'val = ' + '{:d}'.format(item[0]) + ' ' + 'weight = ' + '{:d}'.format(item[1])

		print str(sum_weight) + ' '+ str(sum_val)

knapsack_weight, num = map(int,raw_input().split())

while knapsack_weight!=0 and num!=0:
	items = []
	w =[]
	v = []
	for i in xrange(num):
		x,y = map(int,raw_input().split())
		items.append((x,y))
		items = sorted(items, key=lambda x: x[0])

	for item in items:
		w.append(item[0])
		v.append(item[1])
	#print items
	knapsack_problem(knapsack_weight,w,v)
	raw_input()
	knapsack_weight, num = map(int,raw_input().split())

