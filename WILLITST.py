

t = int(raw_input())


while(True):
    if t==1:
        print("TAK")
        break
    if t%2 == 0:
        t = t//2
    else:
        print("NIE")
        break