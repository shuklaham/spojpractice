
tc = int(raw_input())
for i in range(tc):
    blank = raw_input()
    inp = raw_input().split(' ')
    for j in range(2,len(inp)-1,2):
        if inp[j-1] == '+':
            inp[j] = int(inp[j-2]) + int(inp[j])
            #print inp[j]
        elif inp[j-1] == '-':
            inp[j] = int(inp[j-2]) - int(inp[j])
            #print inp[j]
        elif inp[j-1] == '/':
            inp[j] = int(inp[j-2]) // int(inp[j])
            #print inp[j]
        elif inp[j-1] == '*':
            inp[j] = int(inp[j-2]) * int(inp[j])
            #print inp[j]
    print inp[len(inp)-2]