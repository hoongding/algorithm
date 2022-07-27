from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
box = [[0]*M]*N
q = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = 0

for i in range(N):
    box[i] = input().split()

for i in range(N):
    for j in range(M):
        box[i][j] = int(box[i][j])

for i in range(N): #먼저 1인놈들다 큐에 넣어주기.
    for j in range(M):
        if box[i][j] == 1:
            q.append([i, j])


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append([nx, ny])

bfs()

for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res - 1)
