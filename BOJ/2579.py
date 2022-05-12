size = int(input())
stair = [0]*300


dp = [0]*300
for i in range(size):
    stair[i]= int(input())

dp[0] = stair[0] #0
dp[1]= stair[0]+stair[1] #1
dp[2] = max(stair[0]+stair[2],stair[1]+stair[2]) #2

for i in range(3,size):
    dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])    

print(dp[size-1])
        
