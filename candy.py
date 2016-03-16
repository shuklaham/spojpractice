#spoj solutions
#import math

'''
My solution

def count_steps(carray):
    quo,rem = divmod(sum(carray),len(carray))
    if rem !=0:
        return -1
    if (sum([n==quo for n in carray])) == len(carray):
        return 0
    steps = 0
    for i in range(len(carray)):
        if carray[i] == quo:
            continue
        elif carray[i] < quo:
            for j in range(i+1,len(carray)):
                if carray[j] > quo:
                    diff = carray[j] - quo
                    adj = min(quo-carray[i],carray[j]-quo)
                    carray[i]+= adj
                    steps+= adj
                    carray[j]-=adj
                    if carray[i] == quo:
                        break
    return steps



num_packets = int(raw_input())

while num_packets !=-1:
    l = []
    for i in range(num_packets):
        candies = int(raw_input())
        l.append(candies)
    l.sort()
    print count_steps(l)
    num_packets = int(raw_input())
'''


while True:
    noOfCase=int(raw_input())
    if noOfCase<0:
        break
    else:
        series=[]
        for i in range(noOfCase):
            series.append(int(raw_input()))
        sum1=0
        for i in series:
            sum1+=i
        if sum1%noOfCase==0:
            avg=sum1/noOfCase
            moves=0
            for i in series:
                if (avg-i)<0:
                    moves+=i-avg
            print(moves)
        else:
            print(-1)