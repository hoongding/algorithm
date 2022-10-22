from collections import deque


def solution(n, m, image):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    sector = 0
    for sy in range(n):
        for sx in range(m):
            if image[sy][sx] == float('inf'):
                continue
            current_color = image[sy][sx]
            queue = deque([(sy, sx)])
            image[sy][sx] = float('inf')
            while queue:
                y, x = queue.popleft()

                for dy, dx in directions:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < n and 0 <= nx < m and image[ny][nx] == current_color:
                        image[ny][nx] = float('inf')  # 방문하면 inf로 바꾼다!
                        queue.append((ny, nx))
            sector += 1

    return sector