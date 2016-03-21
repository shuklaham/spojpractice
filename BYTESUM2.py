# hint : http://code.cloudkaksha.org/spoj/spoj-bytesm2-solution

'''
1
6 5
3 1 7 4 2
2 1 3 1 1
1 2 2 1 8
2 2 1 5 3
2 1 4 4 4
5 2 7 5 1

0 3 1 7 4 2 0
0 2 1 3 1 1 0
0 1 2 2 1 8 0
0 2 2 1 5 3 0
0 7 8 11 11 9 0
0 5 2 7 5 1 0
'''

tc = int(raw_input())
for i in range(tc):
    h,w = raw_input().split(' ')
    h = int(h)
    w = int(w)
    inp = []
    for j in range(h):
        row = [int(x) for x in raw_input().split(' ')]
        row = [0] + row + [0]
        inp.append(row)

    for y in range(h-2,-1,-1):
        for x in range(1,w+1):
            inp[y][x] = inp[y][x] + max(inp[y+1][x],inp[y+1][x-1],inp[y+1][x+1])

    ans = max(inp[0])
