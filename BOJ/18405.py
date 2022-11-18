# N, K 입력
from collections import deque

N, K = map(int, input().split())

virus_map = [[0 for _ in range(K)] for _ in range(N)]

print(virus_map)

for i in range(N):  # N개의 줄
    temp_list = input().split()
    virus_map[i] = temp_list


