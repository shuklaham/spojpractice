tc = int(raw_input())
d = {0:[0],1:[1],2:[6,2,4,8],3:[1,3,9,7],4:[6,4],5:[5],6:[6],7:[1,7,9,3],8:[6,8,4,2],9:[1,9]}
for i in range(tc):
    a,b = raw_input().split(' ')
    a = int(a[len(a)-1])
    if int(b) == 0:
        print 1
    elif a in [0,1,5,6]:
        print a
    elif a in [4,9]:
        probables = d[a]
        print probables[int(b)%2]
    elif a in [2,3,7,8]:
        probables = d[a]
        print probables[int(b)%4]
