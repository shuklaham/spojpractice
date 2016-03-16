#spoj solutions
cache = {1:0.5}

def card_length(n):
    s = 0.0
    if n in cache:
        return cache[n]
    s = s + float(1)/(1+n) + card_length(n-1)
    cache[n] = s
    return s

c = float(raw_input())
while c!= 0.0:
    tot = 0.0
    i=1
    while tot < c:
       tot = card_length(i)
       i= i+1
    print str(i-1) + ' card(s)'
    c = float(raw_input())
