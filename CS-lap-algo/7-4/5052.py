# 5052번 전화번호 목록
import sys
input = sys.stdin.readline

def yes_or_no(phone_num):
    for item in phone_num:
        for k in range(phone_num.index(item) + 1, len(phone_num)):
            if len(item) < len(phone_num[k]):
                item2 = phone_num[k][0:len(item)]
                if item == item2:
                    print("NO")
                    return
    print("YES")


for i in range(int(input())):
    test_case = int(input())
    phone_num = []
    for j in range(test_case):
        temp = input().strip('\n')
        phone_num.append(temp)
    phone_num.sort()
    yes_or_no(phone_num)
