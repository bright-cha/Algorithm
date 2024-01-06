import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]
# 공기 청정기 위치 찾기
# for i in range(2, R):
#     if matrix[i][0] == -1:
#         if not up:
#             up = (i, 0)
#         else:
#             down = (i, 0)
#     if down:
#         break

up, down = (), ()
for _ in range(T):
    visited = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            # 공기청청기가 아닌 위치
            if matrix[x][y] != -1:
                if matrix[x][y] >= 5:
                    dust = matrix[x][y] // 5
                    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    for dx, dy in delta:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] != -1:
                            visited[nx][ny] += dust
                            matrix[x][y] -= dust
            elif not down:
                if not up:
                    up = (x, 0)
                else:
                    down = (x, 0)

    # 확산된 먼지 합
    for x in range(R):
        for y in range(C):
            if visited[x][y] != 0 and matrix[x][y] != -1:
                matrix[x][y] += visited[x][y]

# 확산이 끝난 경우
    # 위쪽 공기청청기
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    d = 0
    x, y = up[0] - 1, up[1]
    while True:
        nx, ny = x + delta[d][0], y + delta[d][1]
        if 0 <= nx < R and 0 <= ny < C and nx <= up[0]:
            if matrix[nx][ny] == -1:
                matrix[x][y] = 0
                break
            matrix[x][y] = matrix[nx][ny]
            x, y = nx, ny
        else:
            d = (d + 1) % 4

    # 아래쪽 공기청청기
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    d = 0
    x, y = down[0] + 1, down[1]
    while True:
        nx, ny = x + delta[d][0], y + delta[d][1]
        if 0 <= nx < R and 0 <= ny < C and nx > up[0]:
            if matrix[nx][ny] == -1:
                matrix[x][y] = 0
                break
            matrix[x][y] = matrix[nx][ny]
            x, y = nx, ny
        else:
            d = (d + 1) % 4

ans = 0
for i in range(R):
    for j in range(C):
        if matrix[i][j] != -1:
            ans += matrix[i][j]

print(ans)