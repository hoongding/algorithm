a = int(input())
b = int(input())
c = int(input())
mul_val = a*b*c
num_list = list(str(mul_val))
length = len(num_list)
cnt_list=[]

for i in range(10):
    cnt = 0
    for j in range(length):
        if str(i)==num_list[j]:
            cnt = cnt + 1
    cnt_list.append(cnt)

for i in range(10):
    print(cnt_list[i])
