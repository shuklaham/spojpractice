# Game theory


tc = int(raw_input())
while tc!=0:
    pieces,player = raw_input().split(' ')
    pieces = int(pieces)
    player = int(player)
    if player:
        print 'Pagfloyd wins.'
    else:
        print 'Airborne wins.'
    tc = tc -1