n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
# your code goes here
if max(height) > k:
    print(max(height)-k)
else:
    print(0)
