def solution(arr):
    answer = []
    min_arr_element = min(arr)
    if len(arr) == 1:
        answer.append(-1)
    else:
        for item in arr:
            if item == min_arr_element:
                continue
            answer.append(item)
    return answer