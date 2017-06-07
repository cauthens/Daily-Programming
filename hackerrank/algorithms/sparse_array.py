# 6 - 7 - 2017
# https://www.hackerrank.com/challenges/sparse-arrays

n = int(input())
s_init = [input() for _ in range(n)]
q = int(input())
q_string = [input() for _ in range(q)]

for i in q_string:
    print(s_init.count(i))
