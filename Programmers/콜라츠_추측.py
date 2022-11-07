def solution(num):
    answer = 0
    if num == 1:
        answer = 0
    else:
        for i in range(1,501):
            if num % 2 == 0: #짝수라면
                num //= 2
                if num == 1:
                    answer = i
                    break
            else:
                num = num*3 +1
            if i == 500:
                answer = -1
    return answer