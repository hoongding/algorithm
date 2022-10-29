# 갈색 격자의 수 brown
# 빨간색 격자의 수 red
def solution(brown, red):
    # red 의 약수 구하기.
    # 2 * 12라던가.. 이런식으로?
    answer = []
    m = int(red ** 0.5) + 1
    dict = []
    for i in range(1, m + 1):
        if red % i == 0:
            dict.append((red//i, i))
    for x, y in dict:
        sum = x * 2 + y * 2 + 4
        if sum == brown:
            answer.append(x + 2)
            answer.append(y + 2)
            break
    return answer