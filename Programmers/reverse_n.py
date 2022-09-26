def solution(n):
    n = str(n)
    n_list = list(n)
    n_list.reverse()
    answer = []
    for item in n_list:
        answer.append(int(item))
    return answer