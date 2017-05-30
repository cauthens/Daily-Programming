# 5 - 29 - 17
# https://www.hackerrank.com/challenges/migratory-birds

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
counts = {types.count(i):i for i in range(6,1,-1)}

# your code goes here
print(counts[max( counts.keys() )])
