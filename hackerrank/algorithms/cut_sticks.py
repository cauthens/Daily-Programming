
# https://www.hackerrank.com/challenges/cut-the-sticks
# 6 - 6 - 2017

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr_min = min(arr)

while(len(arr) > 0):
    temp_ind = []

    for i,element in enumerate(arr):
        element -= arr_min
        if element <= 0:
            temp_ind.append(i)

    print(len(arr))

    for i,ind in enumerate(temp_ind):
        arr.pop(ind-i)

    if(len(arr) != 0):
        arr_min = min(arr)
