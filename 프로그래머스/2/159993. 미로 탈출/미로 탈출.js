function solution(maps) {
    const rows = maps.length;
    const cols = maps[0].length;

    let start = null;
    let lever = null;
    let exit = null;

    // 미로에서 'S', 'L', 'E'의 위치를 찾기
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (maps[i][j] === 'S') {
                start = [i, j];
            } else if (maps[i][j] === 'L') {
                lever = [i, j];
            } else if (maps[i][j] === 'E') {
                exit = [i, j];
            }
        }
    }

    // BFS 함수 정의
    const bfs = (startPoint, endPoint) => {
        const queue = [];
        const visited = Array.from({ length: rows }, () => Array(cols).fill(false));
        const directions = [
            [1, 0], // 아래
            [-1, 0], // 위
            [0, 1], // 오른쪽
            [0, -1] // 왼쪽
        ];

        queue.push([startPoint[0], startPoint[1], 0]); // [행, 열, 시간]
        visited[startPoint[0]][startPoint[1]] = true;

        while (queue.length > 0) {
            const [x, y, time] = queue.shift();

            // 도착 지점에 도달했을 때 시간 반환
            if (x === endPoint[0] && y === endPoint[1]) {
                return time;
            }

            for (const [dx, dy] of directions) {
                const nx = x + dx;
                const ny = y + dy;

                // 미로의 범위를 벗어나지 않고, 방문하지 않았으며, 벽이 아닌 경우
                if (
                    nx >= 0 && nx < rows &&
                    ny >= 0 && ny < cols &&
                    !visited[nx][ny] &&
                    maps[nx][ny] !== 'X'
                ) {
                    visited[nx][ny] = true;
                    queue.push([nx, ny, time + 1]);
                }
            }
        }

        // 도착 지점에 도달할 수 없을 때
        return -1;
    };

    // 시작점에서 레버까지의 최단 경로 시간
    const timeToLever = bfs(start, lever);
    if (timeToLever === -1) {
        return -1;
    }

    // 레버에서 출구까지의 최단 경로 시간
    const timeToExit = bfs(lever, exit);
    if (timeToExit === -1) {
        return -1;
    }

    // 총 소요 시간 반환
    return timeToLever + timeToExit;
}
