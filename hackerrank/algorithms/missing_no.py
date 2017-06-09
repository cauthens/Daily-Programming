# https://www.hackerrank.com/challenges/missing-numbers
# 6 - 8 -2017

n = int(input())
A, B = {}, {}
for i in input().split(" "):
    num = int(i)
    if A.get(num):
        A[num] += 1
    else:
        A[num] = 1


m = int(input())

for i in input().split(" "):
    num = int(i)
    if B.get(num):
        B[num] += 1
    else:
        B[num] = 1

akey, bkey = set(A.keys()), set(B.keys())

out_set = list(akey.difference(bkey))

mast_set = akey.union(bkey)


out_set += [keys for keys in mast_set if A[keys] != B[keys]]

for output in out_set:
    print(output,end=" ")
