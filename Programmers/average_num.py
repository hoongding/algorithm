def solution(arr):
    answer = 0
    add_num = 0
    for num in arr:
        add_num += num
    answer = add_num / len(arr)
    return answer