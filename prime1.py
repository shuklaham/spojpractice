#spoj solutions
import math

noofcases = int(raw_input())
i = 1
while i <= noofcases:
    numarr = raw_input().split(" ")
    firstnum = int(numarr[0])
    secondnum = int(numarr[1])

    A = [True]*(secondnum+1)
    A[0] = False
    A[1] = False
    #j = 2
    #while j <= math.sqrt(secondnum):
    for j in xrange(2, int(math.sqrt(secondnum))+1):
        if A[j] == True:
            k=j*j
            mult = 1
            while k<=secondnum:
                A[k]= False
                k= j*j + mult*j
                mult = mult+1
     #   j = j + 1

    for p in xrange(len(A)):
        if (A[p] == True) and (p >= firstnum):
            print p
    if i < noofcases:
        print ""
    i = i+1