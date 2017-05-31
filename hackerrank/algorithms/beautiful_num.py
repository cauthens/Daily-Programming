
# 5 - 30 - 17
#  https://www.hackerrank.com/challenges/beautiful-days-at-the-movies 

i,j,k = [int(i) for i in input().split(" ")]
beautiful = 0
for x in range(i,j+1):
    rev = int(str(x)[::-1])
    if abs(rev-x) % k == 0:
        beautiful += 1

print(beautiful)
