n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
lo, hi, cl, ch = s[0], s[0], 0, 0

for num in s[1:]:
    if num < lo:
        lo = num
        cl+= 1
    elif num > hi:
        hi = num
        ch += 1
print(ch, cl)
