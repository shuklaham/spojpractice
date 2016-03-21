
def breakSquareAdd(n):
    s = 0
    while n!=0:
        temp = n%10
        s = s + temp*temp
        n = n/10
    return s

num = int(raw_input())
lst = []
count = 0
while True:
    a = breakSquareAdd(num)
    count = count + 1
    if a ==1:
        print count
        break
    else:
        if a not in lst:
            lst.append(a)
        else:
            print -1
            break
    num = a

