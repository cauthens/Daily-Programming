import itertools as it
word, count = input().strip().split()
count = int(count)
word = list(word)

x = ["".join(perm) for perm in list(it.permutations(word,count))]
x.sort()
for line in x:
    print(line)
