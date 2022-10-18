# 3개 숫자 더했을때 소수가 되는 경우의 개수
# nums : 숫자들이 들어있는 배열
# 서로다른 3개 골라 더했을 때 가능한 소수가 되는 경우의 개수 return
# 중복 없음.
from itertools import combinations

def is_prime_num(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    sum_list = list(x + y + z for x, y, z in combinations(nums, 3))
    count = 0
    for item in sum_list:
        if is_prime_num(item):
            count += 1

    return count