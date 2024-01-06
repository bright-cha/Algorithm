import sys
sys.stdin = open('input.txt')


import heapq


def dijkstra(start):
    q = []
    # 거리, 위치
    heapq.heappush(q, (0, start))
    dists[start] = 0

    while q:
        # 거리, 위치
        dist, start = heapq.heappop(q)
        # 기록된 거리보다 크다면 패스
        if dist > dists[start]:
            continue

        # 연결된 간선 탐색
        for next in edge[start]:
            # 새로운 정점과 추가 거리
            next_node, cost = next

            # 누적 거리
            new_dist = dist + cost
            # 새로운 위치에 기록된 거리보다 크거나 같다면 패스
            if dists[next_node] <= new_dist:
                continue

            heapq.heappush(q, (new_dist, next_node))
            dists[next_node] = new_dist


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    # 정점의 갯수로 변경
    V += 1

    # 간선 저장
    edge = [[] * V for _ in range(V)]
    for _ in range(E):
        f, t, d = map(int, input().split())
        edge[f].append((t, d))

    # 거리 저장
    dists = [1e9] * V

    dijkstra(0)
    print(f'#{tc}', dists[V - 1])