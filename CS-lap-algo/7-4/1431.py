# 1431번 시리얼번호
serial = []
for i in range(int(input())):
    temp = input()
    serial.append(temp)

for i in range(len(serial)-1):
    for j in range(i+1, len(serial)):
        if len(serial[i]) > len(serial[j]): # 만약 길이가 더 짧으면 바꿔줌
            serial[i], serial[j] = serial[j], serial[i]
        elif len(serial[i]) == len(serial[j]): # 만약 길이가 같다면 숫자 탐색!
            sum1 = 0
            sum2 = 0
            for x, y in zip(serial[i], serial[j]): # 숫자면 sum1, sum2에 더해줌.
                if x.isdigit():
                    sum1 += int(x)
                if y.isdigit():
                    sum2 += int(y)
            if sum1 > sum2: # sum이 더 크다면 바꿔줌
                serial[i], serial[j] = serial[j], serial[i]

            elif sum1 == sum2: # sum 도 같으면 사전순서대로 해야하니까 이렇게 비교!
                for x, y in zip(serial[i], serial[j]):
                    if x > y:
                        serial[i], serial[j] = serial[j], serial[i]
                        break
                    elif x < y:
                        break

for i in serial:
    print(i)





