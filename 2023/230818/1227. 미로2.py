import sys
sys.stdin = open('input.txt')
####################################
def bfs(sti, stj):
    q.append((sti, stj))
    visited[sti][stj] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0, 1], [0, -1],[1, 0],[-1, 0]]:
            ni, nj = di + i, dj + j
            if 0 <= ni < 100 and 0 <= nj < 100:
                if visited[ni][nj] == 0 and maze[ni][nj] != 1:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
    return 0


T = 10
for _ in range(1, T + 1):
    tc = int(input())
    # 미로 크기 100
    maze = [list(map(int, input())) for _ in range(100)]
    # 출발지 찾기
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                sti, stj = i, j

    visited = [[0] * 100 for _ in range(100)]
    q = []

    print(f'#{tc}', bfs(sti, stj))