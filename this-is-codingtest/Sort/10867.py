# 10867번 중복 빼고 정렬하기
N = int(input())
need_sort = list(map(int, input().split()))
need_sort = list(set(need_sort))

need_sort.sort()
for i in range(len(need_sort)):
    print(need_sort[i], end = " ")