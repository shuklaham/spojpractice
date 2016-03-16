#spoj solutions
numofcols = int(raw_input())
sent = raw_input()

while True:
    real_sentence = ''
    for p in range(numofcols):
        d1 = 2*numofcols - (p+1) - p
        nextnum = 2*numofcols - (p+1)
        d2 = 2*p +1
        st = sent[p]
        ind = p
        for q in range((len(sent)/numofcols)-1):
            if (q+1)%2 == 1:
                ind = ind + d1
                st = st + sent[ind]
            else:
                ind = ind + d2
                st = st + sent[ind]
        #print st
        real_sentence = real_sentence + st
    print real_sentence
    numofcols = int(raw_input())
    if numofcols == 0:
        break
    sent = raw_input()
