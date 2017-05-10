time = input().strip().split(":")


if 'PM' in time[-1]:
    if time[0] != '12':
        time[0] = str(int(time[0]) + 12)

elif time[0] == '12':
    time[0] = "00"

time[-1] = time[-1][:-2]
print(":".join(time))
