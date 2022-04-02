div_num = int(input())

div_list = list(map(int, input().split()))

max_num = max(div_list)
min_num = min(div_list)

mul_num = max_num * min_num

print(mul_num)