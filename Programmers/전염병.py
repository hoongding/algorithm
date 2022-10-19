# m,n 가로 세로
# infests 병걸린 직원의 위치
# vaccinateds 백신 맞은 직원 위치
# 이미 다 걸려있으면 0
# 모두 감염 될 수 없다면 -1
# 다 걸리는 시간 return

from collections import deque


def solution(m, n, infests, vaccinateds):
    if m * n - len(infests) - len(infests) == 0:  # 백신, 병 걸린 사람 꽉차있으면 0 return
        return 0

    answer = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque(infests)
    flag = False
    visited = [[0 for _ in range(n)] for _ in range(m)]

    for infest in infests:  # 병, 백신 위치 표시
        visited[infest[0] - 1][infest[1] - 1] = 1
    for vaccinated in vaccinateds:
        visited[vaccinated[0] - 1][vaccinated[1] - 1] = float('inf')

    new_queue = deque([])  # bfs level 세기 위한 새로운 큐.
    while queue:
        y, x = queue.popleft()

        for dy, dx in directions:
            ny = y + dy - 1  # 1부터 세기때문에 -1 해줘서 index 맞춰줌.
            nx = x + dx - 1
            if 0 <= nx < n and 0 <= ny < m and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                flag = True
                new_queue.append([ny + 1, nx + 1])
                infests.append([ny + 1, nx + 1])

        if not queue and new_queue:  # 새로 병에 걸린 사람이 있다면
            answer += 1
            queue = new_queue
            new_queue = deque([])

    if m * n - len(infests) - len(vaccinateds) != 0:
        return -1

    return answer