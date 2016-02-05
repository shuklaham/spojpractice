def get_last_digit():
    last_digit_dict = {0:[0],1:[1], 2:[6,2,4,8],3:[1,3,9,7], 4:[6,4], 5:[5], 6:[6], 7:[1,7,9,3], 8:[6,8,4,2], 9:[1,9]}
    possible_lds = last_digit_dict[int(num[-1])]
    if int(num[-1]) in [2,3,7,8]:
        return possible_lds[int(pw)%4]
    elif int(num[-1]) in [4,9]:
        return possible_lds[int(pw)%2]
    else:
        return possible_lds[0]

for i in range(int(raw_input())):
    num,pw = [x for x in raw_input().split(" ")]
    if int(pw) == 0:
        print 1
    elif int(num[-1]) == 0:
        print 0
    else:
        print get_last_digit()

