# 2606번 바이러스
com_num = int(input())
connect_num = int(input())
connect = [[]*com_num for _ in range(com_num+1)]
cnt = 0
for i in range(connect_num):
    x, y = map(int, input().split())
    connect[x].append(y)
    connect[y].append(x)


def dfs(graph, v, visited, count):
    visited[v] = 1
    for j in graph[v]:
        if visited[j] == 0:
            dfs(graph, j, visited, count)




visited = [0] * (com_num + 1)
dfs(connect, 1, visited, cnt)

print(visited.count(1) -1)

