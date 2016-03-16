#spoj solutions

known = {1:1}

def nsquares(n):
    if n in known:
        return known[n]
    else:
        c = n**2 + nsquares(n-1)
        known[n] = c
        return known[n]

num = int(raw_input())
while num != 0:
    print nsquares(num)
    num = int(raw_input())
