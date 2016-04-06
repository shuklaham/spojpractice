
ct = input()
p12 = 0
p34 = 0
p14 = 0
while ct:
    ct -= 1
    st = raw_input()
    if st == '1/4':
        p14 += 1
    elif st == '3/4':
        p34 += 1
    else:
        p12 += 1
ans = 1
if p14 <= p34:
    ans += p34
    if p12 % 2 == 0:
        ans += p12 / 2
    else:
        ans += p12 / 2 + 1
else:
    ans += p34
    p14 -= p34
    if p12 % 2 == 0:
        ans += p12 / 2
        if p14 % 4 == 0:
            ans += p14 / 4
        else:
            ans += p14 / 4 + 1
    else:
        ans += p12 / 2
        if p14 >= 2:
            ans += 1
            p14 -= 2
            if p14 % 4 == 0:
                ans += p14 / 4
            else:
                ans += p14 / 4 + 1
        else:
            ans += 1
print ans

