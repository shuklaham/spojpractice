

def fact(n):
    if n ==1 or 0:
        return 1
    temp = n*fact(n-1)
    return temp


test_cases = int(raw_input())
for i in range(test_cases):
    num = int(raw_input())
    print fact(num)