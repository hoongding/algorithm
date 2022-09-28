def solution(array, commands):
    # array : [1, 5, 2, 6, 3, 7, 4] 주어진 배열
    # commands : [start, end, result_index] 2차원 배열
    # start-1, end-1 로 해야할듯
    answer = []
    for item in commands:
        temp_arr = array[item[0]-1:item[1]] # temp_arr 생성
        temp_arr.sort()
        temp_res = temp_arr[item[2]-1]
        answer.append(temp_res)
    return answer