# 서로 다른 소수 3개의 합으로 표현하는 경우의 수.
# 경우의 수 return
from itertools import combinations

def solution(n):
    prime_num = [True] * n
    prime_num_list = []
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if prime_num[i] == True:
            for j in range(i + i, n, i):
                prime_num[j] = False
    for i in range(2, len(prime_num)):
        if prime_num[i]:
            prime_num_list.append(i)

    sum_list = list(x + y + z for x, y, z in combinations(prime_num_list, 3))
    count = 0

    for sum in sum_list:
        if sum == n:
            count += 1

    return count