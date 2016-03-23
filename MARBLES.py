
known = {1:1}
def fact(n):
    global known
    if n in known:
        return known[n]
    else:
        t = n * fact(n-1)
        known[n] = t
        return t

def C(n,k):
    num = 1
    for i in range(n,n-k,-1):
        num = num* i
    den = fact(k)
    return num/den

tc = int(raw_input())
for i in range(tc):
    balls,colors = raw_input().split(' ')
    ans = C(int(balls)-1,int(colors)-1)
    print ans