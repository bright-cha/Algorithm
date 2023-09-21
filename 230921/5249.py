import heapq

'''
#####################프림 알고리즘#################
def prim(start):
    # 이동위치와 가중치 담을 리스트 초기화
    q = []
    # 방문 표시 초기화
    visited = [0] * (V + 1)
    # 최소값 사용을 위한 우선순위 q
    heapq.heappush(q, (0, start))   # 가중치, 정점
    # 가중치 합
    sum_v = 0

    while q:
        weight, v = heapq.heappop(q)
        # 방문한 정점이면 패스
        if visited[v]:
            continue
        # 방문 표시
        visited[v] = 1
        # 가중치 합
        sum_v += weight

        # 이어진 정점 찾고
        for next in range(V + 1):
            # 방문 기록없고 이동가능하면 힙 푸쉬
            if graph[v][next] and visited[next] == 0:
                heapq.heappush(q, (graph[v][next], next))

    return sum_v


T = int(input())
for tc in range(1, T + 1):
    # 정점, 간선 수
    V, E = map(int, input().split())

    # 그래프 정보 무방향(양방향) 생성
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        f, t, w = map(int, input().split())
        graph[f][t] = w
        graph[t][f] = w

    min_v = prim(0)
    print(f'#{tc}', min_v)
'''
############ 크루스칼 알고리즘###########

# 대표자 찾기
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


# 다른 대표자 묶기
def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    elif x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())
for tc in range(1, T + 1):
    # 정점, 간선 수
    V, E = map(int, input().split())
    # 총 정점 개수 + 1
    V += 1

    # 간선 정보 입력
    edge = []
    for _ in range(E):
        # 가중치 우선순위로 작성을 위해 가중치도 입력
        f, t, w = map(int, input().split())
        edge.append([f, t, w])

    # 가중치 기준으로 정렬
    edge.sort(key=lambda x: x[2])

    # 정점 대표자 설정을 위한 리스트 초기화
    parents = [i for i in range(V)]

    cnt = 0
    min_v = 0
    # 가중치 낮은 기준으로 나오는 반복문
    for f, t, w in edge:
        # 대표자가 같지 않은 경우
        if find_set(f) != find_set(t):
            # 탐색 정점 1 증가
            cnt += 1
            # 가중치 합
            min_v += w
            # 간선 연결 및 대표자 설정
            union(f, t)
            # 탐색 정점이 모두인 경우 브렠
            if cnt == V:
                break

    print(f'#{tc}', min_v)