def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True: #sign이 true이면 양수
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer