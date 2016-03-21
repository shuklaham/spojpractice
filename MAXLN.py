
#

tc = int(raw_input())
for i in xrange(tc):
    r = float(raw_input())
    res = 4.0*r*r + 0.25
    formatted_res = '{0:.2f}'.format(res)
    print 'Case ' + str(i+1)+': '+ str(formatted_res)