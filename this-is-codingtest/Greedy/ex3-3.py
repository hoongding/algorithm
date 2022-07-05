# 숫자 카드 게임
N, M = map(int, input().split())
min_list = []
for __ in range(0, N):
    data = map(int, input().split())
    min_list.append(min(data))

print(max(min_list))