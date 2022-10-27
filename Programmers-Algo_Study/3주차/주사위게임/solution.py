# moster : 몬스터 있는 위치
# 확률 : 몬스터 만나지 않을 확률에 1000을 곱한 뒤 소수부는 버리기.
from itertools import combinations


def solution(monster, S1, S2, S3):
    answer = -1
    monster.sort()
    # 3 ~ 9 -> 4 ~ 10
    sum = []
    for a in range(1, S1 + 1):
        for b in range(1, S2 + 1):
            for c in range(1, S3 + 1):
                sum.append(a + b + c)
    count = 0
    for item in sum:
        if item + 1 in monster:
            count += 1

    answer = int((len(sum) - count) / len(sum) * 1000)

    return answer