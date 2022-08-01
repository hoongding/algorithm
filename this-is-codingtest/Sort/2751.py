# 2751번 수 정렬하기 2
need_sort = []
for i in range(int(input())):
    need_sort.append(int(input()))

need_sort.sort()

for i in range(len(need_sort)):
    print(need_sort[i])