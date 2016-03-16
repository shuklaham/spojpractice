#spoj solutions
class Stack:
	def __init__(self):
		self.items = []

	def push(self,obj):
		self.items.append(obj)

	def isEmpty(self):
		if len(self.items) == 0:
			return True
		else:
			return False

	def peek(self):
		if len(self.items) !=0:
			return self.items[len(self.items)-1]
		else:
			return False

	def pop(self):
		if len(self.items) !=0:
			return self.items.pop()
		else:
			return False

# 5, 1, 2, 4, 3
n = int(raw_input())
while n != 0:
	s = [int (x) for x in raw_input().split(' ')]
	i = 0
	need = 1
	flag = True
	blackhole = 0
	st = Stack()
	while i < len(s):
		if st.isEmpty() == False and st.peek() == need:
				blackhole = st.pop()
				need+=1
		elif s[i] != need:
			if st.isEmpty() or st.peek() > s[i]:
				st.push(s[i])
			else:
				flag = False
				break

			i+=1
		else:
			blackhole = s[i]
			need = blackhole+1
			i+=1
	if flag == False:
		print 'no'
	else:
		print 'yes'
	n = int(raw_input())



