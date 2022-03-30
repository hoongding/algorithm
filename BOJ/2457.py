inh_num = list(map(int, input().split()))

add_num = 0

for i in range(5):
    add_num = add_num + inh_num[i]*inh_num[i]

ver_num = add_num % 10

print(ver_num)