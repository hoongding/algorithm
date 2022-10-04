def solution(a, b): #a, b 대소관계 정해져 있지 X
    answer = 0
    if a == b:
        answer = a
    elif a > b: # a가 더 큰경우
        for i in range(b, a+1):
            answer += i
    else: # b가 더 큰경우
        for i in range(a, b+1):
            answer += i
    return answer