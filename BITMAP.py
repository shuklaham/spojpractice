
import pprint

#start = (1,4)
def bfs(start):
    global d
    queue = []
    d[start]['predecessor'] = None
    d[start]['distance'] = 0
    d[start]['color'] = 'gray'
    queue.append(start)
    while len(queue) !=0:
        vertex = queue.pop(0)
        for v in [(vertex[0]-1,vertex[1]),(vertex[0],vertex[1]-1),(vertex[0]+1,vertex[1]),(vertex[0],vertex[1]+1)]:
            if d[v]['value']==-1:
                continue
            if d[v]['color'] == 'white':
                d[v]['color'] = 'gray'
                d[v]['predecessor'] = vertex
                prevDist = d[v]['distance']
                d[v]['distance'] = min(d[vertex]['distance'] + 1,prevDist)
                queue.append(v)
        d[start]['color'] = 'black'

def reset():
    global d
    for k in d.keys():
            d[k]['predecessor'] = None
            d[k]['color'] = 'white'


d = {}
tc = int(raw_input())
for t in range(tc):
    inp =[]
    d = {}
    r,c = raw_input().split(' ')
    r = int(r)
    c = int(c)

    inp.append([-1]*(c+2))
    for i in range(int(r)):
        row = [int(x) for x in list(raw_input())]
        row = [-1] + row + [-1]
        inp.append(row)
    inp.append([-1]*(c+2))

#pprint.pprint(inp)

    for row in range(0,r+2):
        for col in range(0,c+2):
            anotherDict = {}
            d[(row,col)] = anotherDict
            anotherDict['value'] = inp[row][col]
            anotherDict['predecessor'] = None
            anotherDict['color'] = 'white'
            anotherDict['distance'] = float('inf')

    for k in d.keys():
        if d[k]['value'] == 1:
            reset()
            bfs(k)

    for row in range(1,r+1):
        expr = ''
        for col in range(1,c+1):
            expr = expr + str(d[(row,col)]['distance']) + ' '
        print expr[0:len(expr)-1]

blankLine = raw_input()
