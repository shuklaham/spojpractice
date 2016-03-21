num_datasets = int(raw_input())
for i in range(num_datasets):
    num = int(raw_input())
    inp = raw_input()
    count = [0]*8
    str1 = 'TTT'
    str2 = 'TTH'
    str3 = 'THT'
    str4 = 'THH'
    str5 = 'HTT'
    str6 = 'HTH'
    str7 = 'HHT'
    str8 = 'HHH'
    for j in range(0,38):
        if inp[j:j+3] == str1:
            count[0] = count[0] + 1
        if inp[j:j+3] == str2:
            count[1] = count[1] + 1
        if inp[j:j+3] == str3:
            count[2] = count[2] + 1
        if inp[j:j+3] == str4:
            count[3] = count[3] + 1
        if inp[j:j+3] == str5:
            count[4] = count[4] + 1
        if inp[j:j+3] == str6:
            count[5] = count[5] + 1
        if inp[j:j+3] == str7:
            count[6] = count[6] + 1
        if inp[j:j+3] == str8:
            count[7] = count[7] + 1
    print str(i+1)+ ' '+ str(count[0]) + ' ' + str(count[1]) + ' ' + str(count[2]) + ' ' + str(count[3]) + ' ' + str(count[4]) + ' ' + str(count[5]) + ' ' + str(count[6]) + ' ' + str(count[7])
