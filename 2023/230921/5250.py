import sys
sys.stdin = open('input.txt')

import heapq


def dijkstra(x, y):
    q = []
    # 위치, 연료 사용량
    heapq.heappush(q, (0, x, y))
    used[x][y] = 0

    while q:
        # 사용량, 위치 / 우선순위 큐는 제일 앞을 기준으로 정렬 되기에 value를 앞으로
        value, x, y = heapq.heappop(q)

        # 기록된 사용량보다 큰 사용량의 경우 패스
        if used[x][y] < value:
            continue

        # 이동가능한 4 방향
        delta = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
        for nx, ny in delta:
            # 범위 내인 경우
            if 0 <= nx < size and 0 <= ny < size:

                # 새로운 사용량구하기
                new_value = value + 1
                # 현 위치보다 다음 위치가 높은 경우 추가 사용량
                if matrix[x][y] < matrix[nx][ny]:
                    new_value += matrix[nx][ny] - matrix[x][y]

                # 기록된 사용량보다 큰 경우 패스
                if used[nx][ny] <= new_value:
                    continue

                used[nx][ny] = new_value
                heapq.heappush(q, (new_value, nx, ny))


for tc in range(1, int(input()) + 1):
    # 크기
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]

    # 방문 표시 / 연료 사용량 표시
    used = [[1e9] * size for _ in range(size)]

    dijkstra(0, 0)
    print(f'#{tc}', used[size - 1][size - 1])