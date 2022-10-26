# m 그램을 담을 수 있는 가방에 사탕을 가득 채우는 경우의 수.
# m : 가방 최대 무게
# weights : 사탕 무게 배열
from itertools import combinations


def solution(m, weights):
    answer = 0
    for i in range(len(weights)):
        combination = list(combinations(weights, i + 1))
        for item in combination:
            if sum(item) == m:
                answer += 1

    return answer