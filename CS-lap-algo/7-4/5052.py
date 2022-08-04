# 5052번 전화번호 목록
import sys
input = sys.stdin.readline

def yes_or_no(phone_num):
    for item in phone_num:
        for k in range(phone_num.index(item) + 1, len(phone_num)): # item 뺀 다음 index부터 확인.
            if len(item) < len(phone_num[k]): # 길이가 같으면 전화번호가 같을 순 없으니까 길이가 긴놈들만 탐색.
                item2 = phone_num[k][0:len(item)] # 뺀 놈의 길이만큼 앞에서 부터 잘라준다.
                if item == item2: # 만약 같으면 NO 출력!
                    print("NO")
                    return
    print("YES") # 다 돌았는데 No를 출력안했으면 Yes를 출력!


for i in range(int(input())):
    test_case = int(input())
    phone_num = []
    for j in range(test_case):
        temp = input().strip('\n')
        phone_num.append(temp)
    phone_num.sort()  # sort만 해도 길이 짧은순으로 sort해줌.
    yes_or_no(phone_num)
