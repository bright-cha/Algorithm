from collections import deque


def is_possible(start):
    visited = [0] * N
    # 위치, 돈
    q = deque([start])
    while q:
        start = q.popleft()
        for e, m in graph[start]:
            if visited[e] == 0:
                q.append(e)
                visited[e] = 1

    if visited[end_city] == 1:
        return True
    else:
        return False


def bfs(start):
    # 위치, 돈
    q = deque([(start, profit[start], [])])
    max_v = [-1e9, [51]]

    if is_possible(start):
        visited = 0
        while q:
            start, money, lst = q.popleft()

            if start == end_city:
                if lst == max_v[1]:
                    visited += 1
                    if visited >= 2:
                        if max_v[0] < money:
                            return 'Gee'
                        else:
                            return max_v[0]

                max_v = [max(max_v[0], money), lst]

            for e, m in graph[start]:
                if start != e:
                    if m in lst:
                        lst.remove(m)
                    lst.append(m)
                    q.append((e, money + m + profit[e], lst))
                # else:
                #     q.append((start, money, lst))
    else:
        return 'gg'


# 도시의 수, 시작 도시, 도착 도시, 교통수단의 개수
N, start_city, end_city, M = map(int, input().split())
# 시작 끝 가격
info_traffic = [list(map(int, input().split())) for _ in range(M)]
# 도시별 이익
profit = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for s, e, m in info_traffic:
    graph[s].append((e, -m))

print(bfs(start_city))