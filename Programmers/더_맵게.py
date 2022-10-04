import heapq

def solution(scoville, K):
    # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    # Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다
    # scoville : 음식의 스코빌 지수를 담은 배열
    # K : 스코빌 지수
    # 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수
    # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다

    cnt = 0  # 몇번 섞었는지
    heapq.heapify(scoville)  # heap으로 만들기.
    min_sco = heapq.heappop(scoville)  # 먼저 제일 작은값 뽑아서 K랑 비교.
    while min_sco <= K:
        mix = min_sco + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mix)
        min_sco = heapq.heappop(scoville)
        cnt += 1

        if len(scoville) == 1:
            if scoville[0] >= K:
                return cnt
            else:
                return -1

    return cnt