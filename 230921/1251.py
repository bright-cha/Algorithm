import sys
sys.stdin = open('input.txt')


import heapq


def dijkstra(start):
    q = [(0, start)]
    visited[start] = 1

    while q:
        sum_dist, start = heapq.heappop(q)
        x, y = start

        if visited[(x, y)] < sum_dist:
            continue

        dist = 0
        for island in edge:
            nx, ny = island
            if island != (x, y):
                if x == nx:
                    dist = ny ** 2 * tax
                elif y == ny:
                    dist = nx ** 2 * tax
                else:
                    dist = (abs(x - nx) ** 2 + abs(y - ny) ** 2) * tax

                dist += sum_dist

                if visited[(nx, ny)] > dist:
                    visited[(nx, ny)] = dist
                    heapq.heappush(q, (dist, (nx, ny)))


for tc in range(1, int(input()) + 1):
    cnt_island = int(input())
    x_island = list(map(int, input().split()))
    y_island = list(map(int, input().split()))
    tax = float(input())

    edge = []
    for pair in zip(x_island, y_island):
        heapq.heappush(edge, pair)

    visited = {}
    for idx, value in enumerate(edge):
        visited.setdefault(value, 1e9)

    dijkstra(edge[0])
    print(visited[edge[-1]])