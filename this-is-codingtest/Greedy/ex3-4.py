# 예제 3-4 1이 될때 까지
import sys
input1 = sys.stdin.readline()

input_num, div_num = map(int, input1.split())
count = 0

while input_num != 1:
    if input_num % div_num == 0:
        input_num = input_num//div_num
        count += 1
    else:
        input_num -= 1
        count += 1

print(count)