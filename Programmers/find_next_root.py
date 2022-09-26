def solution(n):
    answer = 0
    temp = 0
    for i in range(n+1):
        if i*i == n:
            temp = i
            break
    if temp == 0:
        answer = -1
    else:
        answer = (temp+1)**2
    return answer