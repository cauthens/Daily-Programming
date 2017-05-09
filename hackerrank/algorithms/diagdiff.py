"""Given a square matrix of size NxN,
 calculate the absolute difference between the sums of its diagonals.
format
n
rows space separated
 """


n = int(input().strip())
dig1 = 0
dig2 = 0
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    dig1 += a_t[a_i]
    dig2 += a_t[n-a_i-1]
print(abs(dig1-dig2))
