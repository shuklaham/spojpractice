
def is_ap_or_gp(t):
    if (2*t[1]) == (t[0] + t[2]):
        return 'AP'
    else:
        return 'GP'

a,b,c = [int(x) for x in raw_input().split(" ")]
while (a == 0 and b == 0 and c == 0) == False:
    s = is_ap_or_gp((a,b,c))
    if s == 'AP':
        print s, 2*c -b
    else:
        print s, c**2/b
    a,b,c = [int(x) for x in raw_input().split(" ")]
