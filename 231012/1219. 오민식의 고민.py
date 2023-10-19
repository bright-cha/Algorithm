from collections import deque
import sys
input = sys.stdin.readline


# 도착 가능여부
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
    q = deque([(start, profit[start], [start])])

    if is_possible(start):
        visited = 0
        while q:
            start, money, lst = q.popleft()

            if start == end_city:
                temp = []
                for i in lst:
                    if i not in temp:
                        temp.append(i)
                temp = tuple(temp)

                route.setdefault(temp, money)
                if route[temp] < money:
                    return 'Gee'
                elif route[temp] > money:
                    max_v = -1e9
                    for k, v in route.items():
                        max_v = max(max_v, v)
                    return max_v

            for e, m in graph[start]:
                # 도착시 내 위치, 기존 금액 - 요금 + 도착 시 이익, 기록
                q.append((e, money + m + profit[e], lst + [e]))

    else:
        return 'gg'


# 도시의 수, 시작 도시, 도착 도시, 교통수단의 개수
N, start_city, end_city, M = map(int, input().split())
# 시작 끝 가격
info_traffic = [list(map(int, input().split())) for _ in range(M)]
# 도시별 이익
profit = list(map(int, input().split()))

# 출발 도착 요금
graph = [[] for _ in range(N)]
for s, e, m in info_traffic:
    graph[s].append((e, -m))

route = {}

print(bfs(start_city))