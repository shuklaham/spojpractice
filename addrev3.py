#spoj solutions
n=input()
while n>0:
    a, b = [int(x) for x in raw_input().split()]
    sa, sb=str(a)[::-1],str(b)[::-1]
    sr =str( int(sa)+int(sb) )
    sr = sr[::-1]
    print int(sr)
    n=n-1