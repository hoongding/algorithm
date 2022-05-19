size = int(input())
n = []
dp = [0]*11
for i in range(size):
    n.append(int(input()))

dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3,max(n)+1):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

for i in range(size):
    print(dp[n[i]])