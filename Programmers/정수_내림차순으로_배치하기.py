def solution(n):
    answer = ''
    n_list = list(str(n))
    int_list = []
    for item in n_list:
        int_list.append(int(item))
    int_list.sort(reverse=True)
    for item in int_list:
        answer += str(item)
    answer = int(answer)
    return answer