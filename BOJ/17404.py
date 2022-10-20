# 양옆으로만 안같으면 됨.
N = int(input())

dp = [[float('inf') for _ in range(3)] for _ in range(N)]
price = []
answer = float('inf')
for i in range(N):
    price.append(list(map(int, input().split())))

for j in range(3):
    dp[0][j] = price[0][j]
    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + price[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + price[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + price[i][2]

    for check in range(3):
        if check != j:
            answer = min(answer, min(dp[N-1]))

print(answer)