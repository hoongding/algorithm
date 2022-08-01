# 1431번 시리얼번호
from collections import deque
serial = []
sort_serial = []
for i in range(int(input())):
    temp = input()
    serial.append([len(temp), temp])
serial.sort()

to_remove = []
for i in range(len(serial)-1):

    if serial[i][0] < serial[i+1][0]:
        to_remove.append(i)
        sort_serial.append(serial[i])

    else:
        break
for i in range(len(to_remove)):
    serial.remove(serial[to_remove[i]])

# for i in range(len(serial)):



