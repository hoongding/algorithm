from collections import deque
import sys


def bfs(n, k):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        x_list = []
        x = q.popleft()
        if x - 1 >= 0:
            x_list.append(x - 1)
        if x + 1 <= 100000:
            x_list.append(x + 1)
        if x * 2 <= 100000:
            x_list.append(x * 2)

        for i in range(len(x_list)):
            if visited[x_list[i]] == 0:
                visited[x_list[i]] = visited[x] + 1
                q.append(x_list[i])
        for i in range(len(x_list)):
            if x_list[i] == k:
                print(visited[x_list[i]]-1)
                return


input = sys.stdin.readline
visited = [0] * 100001
n, k = map(int, input().split())

bfs(n, k)

