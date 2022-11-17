# 1. 주식 하나 사기
# 2. 원하는 만큼 팔기
# 3. 아무것도 안하기
# 1,2,3 중 하나해야함.
# 10 7 6이면 최대이익 0
# 3 5 9 최대이익 3 5 사고 둘다 팔면 최대이익 10
test_case = int(input())

def solution(days, prices):
    count = 0
    greedy_arr = []
    max_price = 0
    for i in range(days, 0, -1):
        if not greedy_arr:
            greedy_arr.append(prices[i])
            max_price = prices[i]
        elif prices[i] > max_price:
            max_price = prices[i]

for _ in range(test_case):
    days = int(input())
    prices = list(map(int, input().split()))
    print(solution(days, prices))
