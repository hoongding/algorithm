# 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발 가능
# 뒤에 있는 기능은 앞에 있는 기능이 배포될때 같이 배포.
# progresses : 작업의 진도가 적힌 정수 배열
# speeds : 각 작업의 개발속도가 적힌 정수 배열
# 각 배포마다 몇 개의 기능이 배포되는지 return.
# 배포는 하루에 한번만. 하루의 끝.
# 진도율 95% , 개발속도 4% -> 배포는 2일 뒤에.
from collections import Counter


def solution(progresses, speeds):
    complete_days = []
    for progress, speed in zip(progresses, speeds):
        remain_per = 100 - progress
        if remain_per % speed == 0:
            complete_days.append(remain_per // speed)
        else:
            complete_days.append(remain_per // speed + 1)
    for i in range(len(complete_days) - 1):
        if complete_days[i] >= complete_days[i + 1]:
            complete_days[i + 1] = complete_days[i]
        else:
            continue
    result = Counter(complete_days)
    answer = list(result.values())
    return answer
