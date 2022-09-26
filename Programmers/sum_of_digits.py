def solution(n):
    answer = 0
    n = str(n)
    N_list = list(n)
    for item in N_list:
        item = int(item)
        answer += item
    return answer