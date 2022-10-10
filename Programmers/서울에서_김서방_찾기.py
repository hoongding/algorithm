def solution(seoul):
    answer = ''
    cnt = 0
    for item in seoul:
        if item == 'Kim':
            break
        else:
            cnt += 1
    cnt=str(cnt)
    answer = '김서방은 '+cnt+'에 있다'
    return answer