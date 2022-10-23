# 남은 일의 작업량을 숫자로 매기고
# 배상비용을 최소화
# 배상비용 = 각 선박의 완성까지 남은 일의 작업략을 제곱하여 모두 더한 값.
# 1시간 동안 남은 일 중 하나를 골라 작업량 1만큼 처리가능
# N : 조선소에서 작업할 수 있는 시간
# works : 작업량이 담긴 배열
# 최소 배상 비용 return.
from heapq import heappush, heapify, heappop


def solution(N, works):
    if sum(works) <= N:
        return 0

    answer = 0

    for i in range(len(works)):
        works[i] *= -1

    heapify(works)

    for _ in range(N):
        temp = heappop(works)
        temp += 1
        heappush(works, temp)

    for i in range(len(works)):
        answer += works[i] ** 2

    return answer