# 거스름돈 백준 5585문제. 브론즈2
product_money = int(input())
taro_money = 1000
coin_count = 0
changes = taro_money - product_money

coin_list = [500, 100, 50, 10, 1]

for coin in coin_list:
    coin_count += changes // coin
    changes %= coin

print(coin_count)
