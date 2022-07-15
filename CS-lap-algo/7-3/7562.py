# 7562번 나이트의 이동
from collections import deque
#  8 방향 갈수있는지 없는지 체크하는 함수
def bfs(cur_x, cur_y, arr_x, arr_y):
    if cur_x == arr_x and cur_y == arr_y:
        print(0)
        return
    queue = deque()
    queue.append([cur_x, cur_y])
    visited[cur_x][cur_y] = 1
    while queue:
        a, b = queue.popleft()  # 두 원소가 나온다.
        if a == arr_x and b == arr_y:
            print(visited[arr_x][arr_y]-1)
            return
        if a + 2 < board_len and b + 1 < board_len and visited[a+2][b+1] == 0:
            queue.append([a + 2, b + 1])
            visited[a+2][b+1] = visited[a][b] + 1
        if a + 2 < board_len and b - 1 > -1 and visited[a+2][b-1] == 0:
            queue.append([a + 2, b - 1])
            visited[a + 2][b -1] = visited[a][b] + 1
        if a - 2 > -1 and b + 1 < board_len and visited[a-2][b+1] == 0:
            queue.append([a - 2, b + 1])
            visited[a - 2][b + 1] = visited[a][b] + 1
        if a - 2 > -1 and b - 1 > -1 and visited[a-2][b-1] == 0:
            queue.append([a - 2, b - 1])
            visited[a - 2][b - 1] = visited[a][b] + 1
        if a + 1 < board_len and b + 2 < board_len and visited[a+1][b+2] == 0:
            queue.append([a + 1, b + 2])
            visited[a + 1][b + 2] = visited[a][b] + 1
        if a + 1 < board_len and b - 2 > -1 and visited[a+1][b-2] == 0:
            queue.append([a + 1, b - 2])
            visited[a + 1][b -2] = visited[a][b] + 1
        if a - 1 > -1 and b + 2 < board_len and visited[a-1][b+2] == 0:
            queue.append([a - 1, b + 2])
            visited[a -1][b + 2] = visited[a][b] + 1
        if a - 1 > -1 and b - 2 > -1 and visited[a-1][b-2] == 0:
            queue.append([a - 1, b - 2])
            visited[a -1][b -2] = visited[a][b] + 1



n = int(input())  # 테스트 케이스 개수
for _ in range(n):
    board_len = int(input())  # 체스판 한변의 길이 l*l, 0 ~ l-1
    cur_x, cur_y = map(int, input().split())
    arr_x, arr_y = map(int, input().split())
    visited = [[0] * board_len for i in range(board_len)]  # visited 하나씩 다 만들어줌
    bfs(cur_x, cur_y, arr_x, arr_y)



