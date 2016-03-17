def mergeSort(a):
    if len(a)<=1:
        return (a,0)
    else:
        left,li = mergeSort(a[0:len(a)/2])
        right,ri = mergeSort(a[len(a)/2:len(a)])
        combined,z = merge(left,right)
        return (combined,li + ri + z)

def merge(left,right):
    c = []
    i = 0
    j = 0
    count = 0
    for p in range(0,len(left)+len(right)):
        if i >= len(left):
            c = c + right[j:]
            break
        elif j >= len(right):
            c = c + left[i:]
            break
        if left[i] < right[j]:
            c.append(left[i])
            i+=1
        else:
            c.append(right[j])
            j+=1
            count = count + len(left)-i
        p+=1
    ans = (c,count)
    return ans


tc = int(raw_input())
blank = raw_input()
for i in range(tc):
    l = int(raw_input())
    a = []
    for j in range(l):
        a.append(int(raw_input()))
    blank = raw_input()
    b = mergeSort(a)
    print b[1]