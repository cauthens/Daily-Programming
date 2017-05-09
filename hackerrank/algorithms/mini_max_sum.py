arr = list(map(int, input().strip().split(' ')))

high_sum = 0
low_sum = sum(list(map(abs,arr)))


for i in range(5):
    plc = arr.pop(0)
    if high_sum < sum(arr):
        high_sum = sum(arr)
    if low_sum > sum(arr):
        low_sum = sum(arr)
    arr.append(plc)

print(low_sum, high_sum)
