need_to_money = int(input())
count = 0

coin_type = [500, 100, 50, 10]
for coin in coin_type:
    count += need_to_money // coin
    need_to_money %= coin

print(count)
