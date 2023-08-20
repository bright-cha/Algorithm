import sys
sys.stdin = open('input.txt')
##################################
def bfs(sti, stj, size): # 출발지와 도착지
    q.append((sti, stj))                     # 출발지 인큐
    visited[sti][stj] = 1                     # 출발지 방문기록
    while q:                     # 큐에 정점이 남았다면
        x, y = q.pop(0)                     # 디큐
        if maze[x][y] == 3:                     # 도착했다면
            return visited[x][y] - 2            # 시작할 때 +1과 이 전단계에서의 +1을 빼주기위해 -2
        for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:    # 델타탐색을 통해 길찾기
            ni = x + i
            nj = y + j
            if 0 <= ni < size and 0 <= nj < size:          # 범위 체크
                if visited[ni][nj] == 0 and maze[ni][nj] != 1:   # 벽인지와 방문기록 체크
                    q.append((ni, nj))            # 인큐
                    visited[ni][nj] = visited[x][y] + 1   # 도착기록 + 횟수 증가
    return 0


T = int(input())
for tc in range(1, T+1):
    size = int(input())
    maze = [list(map(int, input())) for _ in range(size)]
    visited = [[0] * size for _ in range(size)]
    q = []
    # 출발지 구하기
    sti = stj = 0
    for i in range(size):
        for j in range(size):
            if maze[i][j] == 2:
                sti, stj = i, j

    print(f'#{tc}', bfs(sti, stj, size))