# From Algorithms warm up
# take input as array an int and clean it
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

zer,pos,neg = 0,0,0
# iterate through the array and keep counts
for i in arr:
    if i < 0:
        neg += 1
    elif i > 0:
        pos += 1
    else:
        zer += 1
# print the results 
print("{}\n{}\n{}".format((pos/n),(neg/n),(zer/n)))
