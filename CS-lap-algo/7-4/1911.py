# 1911 흙길 보수하기
import math
hole = []
N, L = map(int, input().split())
for i in range(N):
    hole.append(list(map(int, input().split())))

hole.sort()
res = 0
bridgeEnd = 0
for a, b in hole:
    if a <= bridgeEnd:  # 덮은 널빤지가 구덩이의 시작점보다 크면! , 겹친다면
        a = bridgeEnd + 1  # 시작점을 널빤지 마지막덮은지점 +1 로 설정한다.
        if b <= a:  # 설정했는데 끝지점보다 더 덮어버리면 널빤지를 안덮어도 된다
            continue
    temp = b - a
    curRes = math.ceil(temp/L)
    res += curRes
    bridgeEnd = a + curRes * L - 1  # 널빤지의 끝 지점은 시작점 에서 널빤지를 덮은 곳 -1 이다. 만약 1-6 이면 1 + 3*2로 덮을 수 있다.

print(res)
