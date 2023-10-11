def dfs(x, y, direction):
    global cnt
    if matirix[x][y] == 0:
        matirix[x][y] = 2
        cnt += 1

    temp = 1
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and matirix[nx][ny] == 0:
            temp = 0
            direction = (direction - 1) % 4
            nx, ny = x + delta[direction][0], y + delta[direction][1]
            if 0 <= nx < N and 0 <= ny < M and matirix[nx][ny] == 0:
                return dfs(nx, ny, direction)
                break
            return dfs(x, y, direction)
            break
    if temp:
        direction = (direction + 2) % 4
        nx, ny = x + delta[direction][0], y + delta[direction][1]
        if 0 <= nx < N and 0 <= ny < M:
            if matirix[nx][ny] == 1:
                return
            else:
                direction = (direction + 2) % 4
                return dfs(nx, ny, direction)


N, M = map(int, input().split())
# r,c 로봇 청소기 위치 / d 바라보는 방향
r, c, d = map(int, input().split())
matirix = [list(map(int, input().split())) for _ in range(N)]

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cnt = 0
dfs(r, c, d)
print(cnt)


