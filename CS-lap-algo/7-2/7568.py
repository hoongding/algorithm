# 7568번 덩치

import sys

people_num = int(sys.stdin.readline())
people_info = []
result = []
for i in range(people_num):
    x, y = map(int, sys.stdin.readline().split())
    people_info.append([x, y])

for i in range(people_num):
    count = 0
    for j in range(people_num):
        if people_info[i][0] < people_info[j][0]:
            if people_info[i][1] < people_info[j][1]:
                count += 1

    result.append(count + 1)

for i in result:
    print(i, end=' ')
