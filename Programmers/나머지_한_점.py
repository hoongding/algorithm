# v : 점 3개의 좌표 들어있는 배열.
from collections import Counter


def solution(v):
    answer = []
    x_list = []
    y_list = []

    for item in v:
        x_list.append(item[0])
        y_list.append(item[1])

    x_count = Counter(x_list)
    y_count = Counter(y_list)
    for i in x_list:
        if x_count.get(i) == 1:
            answer.append(i)
    for i in y_count:
        if y_count.get(i) == 1:
            answer.append(i)
    return answer