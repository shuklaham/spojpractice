

for _ in xrange(int(raw_input())):
    raw_input()
    expr = raw_input().split(' ')
    ans = 0
    opr = '+'
    for p in expr:
        try:
            a = int(p)
            if opr == '+':
                ans += a
            elif opr == '/':
                ans //= a
            elif opr == '-':
                ans -= a
            elif opr == '*':
                ans *= a
        except:
            opr = p
    print ans
