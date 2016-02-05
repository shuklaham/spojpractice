
import math

n = int(raw_input())
total = 0
while n >0:
    c = 0
    limit = math.sqrt(n)
    i = 1
    while i <= limit:
        if n % i == 0:
            c+=1
        i+=1
    total= total+ c
    n=n-1
print total
