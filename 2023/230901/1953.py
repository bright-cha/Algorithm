from collections import deque


def move(sr, sc, time, row, col):
    visited = [[0] * col for _ in range(row)]
    que = deque([(sr, sc, 1)])
    visited[sr][sc] = 1
    cnt = 1

    while que:
        sr, sc, temp_time = que.popleft()

        if temp_time == time:
            break

        for tunnel in tunnels[matrix[sr][sc]]:
            i, j = tunnel[0], tunnel[1]
            ni, nj = sr + i, sc + j
            if 0 <= ni < row and 0 <= nj < col and matrix[ni][nj] != 0:
                if not visited[ni][nj] and (-i, -j) in tunnels[matrix[ni][nj]]:
                    # 1. 통로가 이어진 경우
                    visited[ni][nj] = 1
                    cnt += 1
                    que.append((ni, nj, temp_time + 1))

    return cnt

tunnels = {
    1: [(0, 1), (1, 0), (-1, 0), (0, -1)], 2: [(-1, 0), (1, 0)], 3: [(0, 1), (0, -1)],
    4: [(-1, 0), (0, 1)], 5: [(1, 0), (0, 1)], 6: [(1, 0), (0, -1)], 7: [(-1, 0), (0, -1)]}


T = int(input())
for tc in range(1, T + 1):
    row, col, start_row, start_col, time = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(row)]

    print(f'#{tc}', move(start_row, start_col, time, row, col))



########################## 틀린 코드 / 안가는 루트가 존재한다.
# def move(sr, sc, t):
#     global cnt
#     if t == 0:
#         return
#
#     for tunnel in tunnels[matrix[sr][sc]]:
#         i, j = tunnel[0], tunnel[1]
#         ni, nj = sr + i, sc + j
#         if 0 <= ni < row and 0 <= nj < col and matrix[ni][nj] != 0:
#             if (ni, nj) not in visited and (-i, -j) in tunnels[matrix[ni][nj]]:
#                 # 1. 통로가 이어진 경우
#                 cnt += 1
#                 visited.append((ni, nj))
#                 move(ni, nj, t - 1)
#
#
# tunnels = {
#     1: [(0, 1), (1, 0), (-1, 0), (0, -1)], 2: [(-1, 0), (1, 0)], 3: [(0, 1), (0, -1)],
#     4: [(-1, 0), (1, 0)], 5: [(1, 0), (0, 1)], 6: [(1, 0), (-1, 0)], 7: [(-1, 0), (0, -1)]}
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     row, col, start_row, start_col, time = map(int, input().split())
#     matrix = [list(map(int, input().split())) for _ in range(row)]
#
#     cnt = 1
#     visited = [(start_row, start_col)]
#     move(start_row, start_col, time - 1)
#     print(f'#{tc}', cnt)
