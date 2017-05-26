
# 5 - 25 - 2017
# https://www.hackerrank.com/challenges/extra-long-factorials
n = int(input().strip())
fact = 1
for i in range(n,1,-1):
    fact *= i
print(fact)