import itertools as it
a = [int(x) for x in input().strip().split()]
b = [int(x) for x in input().strip().split()]

c = it.product(a,b)

for x in c:
    print(x, end=" ")
