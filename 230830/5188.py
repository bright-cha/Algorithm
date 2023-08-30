def bfs(x, y):
    global min_v
    if visited[x][y] > min_v:
        return

    if x == size - 1 and y == size - 1:
        if visited[x][y] < min_v:
            min_v = visited[x][y]

    else:
        nx, ny = que.pop(0)
        for di, dj in delta:
            ni, nj = nx + di, ny + dj
            if 0 <= ni < size and 0 <= nj < size:
                visited[ni][nj] = matrix[nx][ny] + matrix[ni][nj]
                que.append((ni, nj))
                bfs(ni, nj)


T = int(input())
for tc in range(1, T + 1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    visited = [[0] * size for _ in range(size)]
    visited[0][0] = matrix[0][0]
    delta = [(0, 1), (1, 0)]
    min_v = 1e9
    sum_v = 0
    que = [(0, 0)]

    bfs(0, 0)
    print(f'#{tc}', min_v)

