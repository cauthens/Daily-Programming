# https://www.hackerrank.com/challenges/angry-professor
# 6 - 10 - 2017

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ') if int(a_temp) <= 0]
    if len(a) >= k:
        print("NO")
    else:
        print("YES")
