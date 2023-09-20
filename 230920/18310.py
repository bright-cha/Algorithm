def dfs(idx, edge_info, visited):
    # 방문지 표시 및 출력
    visited[idx] = 1
    print(idx, end='')
    # 연결 정보
    for i in edge_info[idx]:
        # 방문 확인
        if visited[i] == 0:
            dfs(i, edge_info, visited)


# 정점, 간선수
num, edge = map(int, input().split())
# 임시 리스트 - 간선 정보
temp = list(map(int, input().split()))

# 간선 정보
edge_info = [[] for _ in range(num + 1)]
# 왕복 입력
for i in range(edge):
    v1, v2 = i * 2, i * 2 + 1
    edge_info[temp[v1]].append(temp[v2])
    edge_info[temp[v2]].append(temp[v1])
# 방문 표시 초기화
visited = [0] * (num + 1)
# 함수호출
dfs(1, edge_info, visited)