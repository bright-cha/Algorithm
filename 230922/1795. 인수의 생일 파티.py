import heapq


def dijkstra(start):
    # 시간 위치
    heap = [(0, start)]
    # 방문기록
    visited = [1e9] * (V + 1)
    visited[start] = 0

    while heap:
        # 시간 위치
        w, t = heapq.heappop(heap)

        # 누적합이 최종 목표 지점의 누적합보다 크거나 같은 경우 패스
        if start != X and visited[X] <= w:
            continue

        # 방문한 지역인 경우 패스
        if visited[t] < w:
            continue

        # 방문 기록
        visited[t] = w

        # 연결된 정점과 시간
        for nt, nw in edge[t]:
            # 방문하지 않은 지점인 경우
            if visited[nt] > w + nw:
                heapq.heappush(heap, (w + nw, nt))

    return visited


for tc in range(1, int(input()) + 1):
    V, E, X = map(int, input().split())
    # 간선 정보 입력
    edge = [[] for _ in range(V + 1)]
    for _ in range(E):
        f, t, w = map(int, input().split())
        edge[f].append((t, w))

    # 최대값
    max_v = 0

    # X에서 각 정점까지 오고가는 시간 확인
    v2 = dijkstra(X)

    # 각 정점에서 X까지 시간 구하기
    for i in range(1, V + 1):
        # i까지 오고가는 시간 더하기
        temp = v2[i] + dijkstra(i)[X]
        max_v = max(max_v, temp)
    print(f'#{tc}', max_v)