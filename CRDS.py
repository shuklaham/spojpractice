

tc = int(raw_input())
for i in range(tc):
    level = int(raw_input())
    flatCards = (level-1)*(level)/2
    pairsCards = (level * (level + 1))
    print (flatCards + pairsCards) % 1000007
