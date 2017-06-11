def super_digit(x):
    p_list = map( int, list(x) )
    z = 0
    for i in p_list:
        z += i
    return str(z)


n ,k = input().strip().split(" ")
p = n * int(k)


while len(super_digit(p)) > 1:
    p = super_digit(p)

print(super_digit(p))
