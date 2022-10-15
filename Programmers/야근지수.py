# 야근 피로도 = 야근시작한 시점에 남은 일의 작업량 제곱하여 더한값?
# 한시간에 작업량 1
# n : 퇴근까지 남은 시간
# works : 각 일에 대한 작업량
# 4, 3, 3 -> 4시간동안 -> 2, 2, 2로 만들면 야근할때 제일 적은 피로도.
from heapq import heapify, heappop, heappush


def solution(n, works):
    if sum(works) <= n:  # 남아있는 works 총합이 n 보다 작다면 0 리턴
        return 0
    answer = 0

    for i in range(len(works)):  # max heap 구현.
        works[i] *= -1

    heapify(works)

    for _ in range(n):
        temp = heappop(works)
        temp += 1
        heappush(works, temp)
    for i in range(len(works)):
        answer += works[i] ** 2

    return answer