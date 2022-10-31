# 스코빌 지수 K 이상 되도록
# 지수가 가장 낮은 두개 음식을 섞은 음식
# 스코빌 = min 스코빌 + (두번째 min 스코빌 * 2)
# 스코빌 K 이상 될 때까지 섞음.
# scoville : 음식의 스코빌 지수 배열
# K : 스코빌 지수.
# K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # heap으로 만들기.
    min_sco = heapq.heappop(scoville)
    while min_sco < K:
        temp = min_sco + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, temp)
        answer += 1
        if len(scoville) == 1:
            if scoville[0] >= K:
                return answer
            else:
                return -1
        min_sco = heapq.heappop(scoville)

    return answer
