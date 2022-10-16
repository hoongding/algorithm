# 삼각그래프 위쪽 가운데 정점 -> 아래쪽 가운데 정점 최단경로
# 사이클 없음 정점에 비용이 있다.
# 지나간 정점의 비용합
# 가로는 무조건 3줄

temp = int(input())
count = 1
while 1:
    N = temp  # 몇 줄인지 입력
    graph = [[0 for _ in range(3)] for _ in range(N)]
    dp = [[0 for _ in range(3)] for _ in range(N)]

    # 그 정점에서 갈 수 있는 방향 오른쪽 or 아래쪽 3개.

    for y in range(N):
        temp1, temp2, temp3 = map(int, input().split())
        graph[y][0], graph[y][1], graph[y][2] = temp1, temp2, temp3

    dp[1][0] = graph[1][0] + graph[0][1]
    dp[1][1] = graph[1][1] + min(dp[1][0], graph[0][1], graph[0][2] + graph[0][1])
    dp[1][2] = graph[1][2] + min(dp[1][1], graph[0][1], graph[0][1] + graph[0][2])
    for i in range(2, N):
        for j in range(3):
            if j == 0:
                dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + graph[i][0]
            elif j == 1:
                dp[i][1] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0]) + graph[i][1]
            elif j == 2:
                dp[i][2] = min(dp[i][1], dp[i-1][2], dp[i-1][1]) + graph[i][2]
    print(str(count)+". "+str(dp[N-1][1]))

    count += 1
    temp = int(input())
    if temp == 0:
        break


