size = int(input())
money = []
for _ in range(size):
    money.append(int(input()))
realMoney = []

for i in range(len(money)):
    if money[i] == 0 :
       realMoney.pop()
    else : realMoney.append(money[i])
sumMoney = sum(realMoney)
print(sumMoney)    
        
    