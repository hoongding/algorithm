# 1253번 좋다
import sys

num_len = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
res = 0
num_list.sort()  # 작은 순서대로 일단 정렬!
for i in range(num_len):
    temp = num_list[0:i]+num_list[i+1:]
    left = 0
    right = num_len - 2
    while left < right:
        t = temp[left] + temp[right]
        if t == num_list[i]:
            res += 1
            break
        if t < num_list[i]:
            left += 1
        else:
            right -= 1
print(res)