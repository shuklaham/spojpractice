
import math
b = int(raw_input())
while b!= -1:
    t = str(math.sqrt(9+12*(b-1)))
    if len(t.split('.')[1]) >1:
        print 'N'
    else:
        print 'Y'
    b = int(raw_input())
