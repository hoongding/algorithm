# 11651 좌표 정렬하기2
need_sort = []
for i in range(int(input())):
    x, y = map(int, input().split())
    need_sort.append([y, x])

need_sort.sort()

for i in range(len(need_sort)):
    print(need_sort[i][1], need_sort[i][0])