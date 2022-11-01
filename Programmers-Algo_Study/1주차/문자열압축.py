# aabbaccc -> 2a2ba3c : 문자가 반복되지 않아 한번만 나타난 경우 1은 생략함.
# 1개 이상의 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return
# 압축할 문자열 s
def solution(s):
    s_list = list(s)  # 문자열 리스트로.
    res_list = []
    for i in range(1, len(s) + 1):  # 길이만큼 돌려보자, i 는 자를 개수.
        res_list.append(slice_s(s, i))
    answer = min(res_list)
    return answer


def slice_s(s, length):  # length는 자르려는 문자열 길이.
    iter_num = len(s) // length  # 반복할 횟수
    remainder = len(s) % length
    temp = []
    temp_res = ''
    for i in range(iter_num):
        temp.append(s[i * length:(i * length) + length])
    if remainder != 0:
        temp.append(s[-remainder:])

    repeat_num = 0
    for i in range(len(temp) - 1):
        if temp[i] != temp[i + 1]:
            if repeat_num != 0:
                temp_res = temp_res + str(repeat_num + 1) + temp[i]
                repeat_num = 0
            else:
                temp_res = temp_res + temp[i]
        else:
            repeat_num += 1
    if repeat_num != 0:
        temp_res = temp_res + str(repeat_num) + temp[-1]
    else:
        temp_res = temp_res + temp[-1]
    return len(temp_res)