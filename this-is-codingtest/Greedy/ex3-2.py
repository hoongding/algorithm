# 큰 수의 법칙
import sys

N, M, K = map(int, sys.stdin.readline().split())

number_list = list(map(int, sys.stdin.readline().split()))

number_list.sort(reverse=True)
first_max_num = number_list[0]
second_max_num = number_list[1]
one_cycle = first_max_num * K + second_max_num

result = (M // (K+1)) * one_cycle + (M % (K+1)) * first_max_num

print(result)
