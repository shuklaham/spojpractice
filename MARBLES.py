
from math import factorial


def C(n,r):
    if r > (n // 2):
        r = n - r
    k = n
    ans = 1
    while k != (n - r):
        ans *= k
        k -= 1
    return ans // factorial(r)

tc = int(raw_input())
for i in range(tc):
    balls,colors = raw_input().split()
    ans = C(int(balls)-1,int(colors)-1)
    print ans