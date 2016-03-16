#spoj solutions
t = int(raw_input())
for i in range(t):
    N = int(raw_input())
    list1 = [int(x) for x in raw_input().split(" ")]
    list2 = [int(x) for x in raw_input().split(" ")]

    list1.sort(reverse=True)
    list2.sort(reverse=True)

    print sum([int(i)*int(j) for (i, j) in zip(list1, list2)])

'''
test = int(raw_input())
while test>0:
    test-=1
    n=int(raw_input())
    guy=sorted(map(int,raw_input().split()))[::-1]
    girl=sorted(map(int,raw_input().split()))[::-1]
    sum = 0
    for i in range(0,n):
        sum+= guy[i]*girl[i]
    print sum'''