def sum_of_digit(x):
    x = str(x)
    x_list = list(x)
    sum = 0
    for item in x_list:
        sum += int(item)
    return sum

def solution(x):
    answer = True
    if x % sum_of_digit(x) != 0:
        answer = False
    return answer