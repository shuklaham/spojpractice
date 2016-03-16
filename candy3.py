#spoj solutions
t = int(raw_input())
while t >=1:
    space = raw_input()
    num_childs = int(raw_input())
    candy_list = []
    for i in range(num_childs):
        candy = int(raw_input())
        candy_list.append(candy)
    if sum(candy_list) % num_childs == 0:
        print "YES"
    else:
        print "NO"
    t = t-1