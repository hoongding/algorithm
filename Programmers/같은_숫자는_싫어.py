def solution(arr):
    # 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다
    # 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
    answer = []
    answer.append(arr[0])
    cnt = 0
    for i in range(1, len(arr)):
        if arr[i] == answer[cnt]:
            continue
        else:
            answer.append(arr[i])
            cnt += 1

    return answer