# n^2 greedy aproach to absolute minimum difference
# 6 - 13 - 2017
# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
low = abs(min(a)-max(a))
# your code goes here
for i in range(n):
    for j in range(n):
        temp = abs(a[i]-a[j])
        if i != j and temp < low:
            low = temp
print(low)
