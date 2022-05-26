day, ddeok = map(int,input().split())

dp = [[0]*2 for _ in range(day+1)]

dp[1][0] = 1
dp[1][1] = 0 

dp[2][0] = 0
dp[2][1] = 1

dp[3][0] = 1
dp[3][1] = 1

for i in range(4, day+1):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = dp[i-1][0] + dp[i-1][1]

first_day = dp[day][0]
second_day = dp[day][1]

loop_num = ddeok // first_day

for i in range(1, loop_num+1):
    remain_ddeok = ddeok - (first_day*i)
    if remain_ddeok%second_day ==0:
        second_day = remain_ddeok//second_day
        first_day = i
        break

print(first_day)
print(second_day) 
