def solution(x, n): # x부터 시작해서 x씩 증가하는 숫자 n개 리스트 리턴
    answer = []
    for i in range(n):
        answer.append(x+x*i)
    return answer