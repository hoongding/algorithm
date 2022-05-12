num = int(input())
dp = []
dp.append(0) #! 0
dp.append(0) #! 1
dp.append(1) #! 2
dp.append(1) #! 3

def find_min_num(num):
    for i in range(4,num+1):      
        if (i%3 == 0 and i%2 == 0):
            dp.append(min(dp[i-1]+1,dp[i//3]+1,dp[i//2]+1))
        elif i%3 == 0:
            dp.append(min(dp[i-1]+1,dp[i//3]+1))
        elif i%2 == 0:
            dp.append(min(dp[i-1]+1,dp[i//2]+1))
        else : 
            dp.append(dp[i-1]+1)
            
            
find_min_num(num)
print(dp[num])
