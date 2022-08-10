#  2343번 기타 레슨
lecture_num, sector = map(int, input().split())
lecture = list(map(int, input().split()))
res = 0

for i in range(lecture_num):
    temp = lecture[i]
    res += temp

avg = res//sector
sum_list = []
temp = 0
k = avg
while 1:
    for i in range(lecture_num):
        if temp+lecture[i] == k: # 같으면 그냥 끊어?
            sum_list.append(temp+lecture[i])
            temp = 0
            continue
        elif temp+lecture[i] > k: # 만약 temp가 avg보다 크면
            a = temp+lecture[i] - k
            b = k - temp
            if a > b: # 만약 더한 놈보다 그전이 avg보다
                sum_list.append(temp)
                temp = 0
            else:
                sum_list.append(temp+lecture[i])
                temp = 0
                continue
        temp += lecture[i]
    if len(sum_list) == sector:
        break
    k += 1

print(max(sum_list))


