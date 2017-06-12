# https://www.hackerrank.com/challenges/icecream-parlor
# 6 - 12 - 2017


k = int(input())
for i in range(k):
    m,n = int(input()),int(input())
    p = [int(z) for z in input().split(" ")]
    pair = []

    for x in range(n):

        for y in range(n):
            if p[x] + p[y] == m and x != y:
                if x > y:
                    pair = [y,x]
                else:
                    pair = [x,y]


    print(pair[0]+1,pair[1]+1)

                
