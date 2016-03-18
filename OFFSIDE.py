
A,D = raw_input().split(' ')
A = int(A)
D = int(D)
while A!=0 and D!=0:
    alist = [int(x) for x in raw_input().split(' ')]
    dlist = [int(x) for x in raw_input().split(' ')]
    alist.sort()
    dlist.sort()
    if alist[0]>= dlist[1]:
        print 'N'
    else:
        print 'Y'
    A,D = raw_input().split(' ')
    A = int(A)
    D = int(D)


