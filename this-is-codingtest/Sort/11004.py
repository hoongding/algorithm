# 11004번 K번째 수
N, K = map(int, input().split())
need_sort = list(map(int, input().split()))
need_sort.sort()
print(need_sort[K-1])
