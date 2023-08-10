import sys
sys.stdin = open("input.txt")
###########################################################
def dfs(start):
    visited[start] = 1
    for w in adj_m[start]:
        if not visited[w]:
            dfs(w)


T = 10
for _ in range(1, T + 1):
    # 테스트 케이스, 간선의 수
    tc, edge = map(int, input().split())
    # 간선 정보 리스트로 받기
    edge_info = list(map(int, input().split()))

    # 이동가능한 정점, 즉 간선의 정보를 담기 위한 행렬 생성
    adj_m = [[] for _ in range(100)]
    for i in range(edge):
        # v1은 현위치에서 v2 이동가능한 위치를 구하고
        v1, v2 = edge_info[i * 2], edge_info[i*2 + 1]
        # v1 위치 인덱스 리스트에 v2를 추가한다.
        adj_m[v1].append(v2)

    # 각 인덱스를 오름차순한다.
    for i in range(100):
        adj_m[i].sort()

    # 방문기록 리스트 생성
    visited = [0] * 100

    # 함수호출
    dfs(0)

    # 99인덱스 방문했으면 1 아니면 0출력
    if visited[99] == 1:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)