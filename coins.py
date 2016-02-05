

cache = {0:0}

def change(num):
    if num in cache:
        return cache[num]
    else:
        cache[num] = max(num, change(num / 4) + change(num / 3) + change(num / 2))
        return cache[num]

for i in range(2):
    n = int(raw_input())
    print change(n)


