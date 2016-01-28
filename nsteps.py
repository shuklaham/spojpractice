
known_center = {(0,0):0}
known_intercept = {(2,0):2}

def intercept_line(p1):
    '''print p1[0]
    print p1[1]
    print 'I am on intercept line'
    '''
    if p1 in known_intercept:
        return known_intercept[p1]
    else:
        t = (p1[0]-1),(p1[1]-1)
        c = intercept_line(t)
        if c%2 == 0:
            known_intercept[p1] = c+1
        else:
            known_intercept[p1] = c+3
        return known_intercept[p1]


def center_line(p2):
    #print p2[0]
    #print p2[1]
    #print 'I am on center line'

    if p2 in known_center:
        return known_center[p2]
    else:
        t = (p2[0]-1),(p2[1]-1)
        c = center_line(t)
        if c%2 == 0:
            known_center[p2] = c+1
        else:
            known_center[p2] = c+3
        return known_center[p2]


num_of_points = int(raw_input())
for i in range(num_of_points):
    a,b = [int(x) for x in raw_input().split(" ")]
    t = a,b
    if a == b:
        print center_line(t)
    elif a == (b + 2):
       print intercept_line(t)
    else:
        print 'No Number'

