'''
V E
v1 w1 v2 v2 ...
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
'''
def dfs(n, V, adj_m):
    stack = []               # stack 생성
    visited = [0] * (V+1)    # visited 생성
    visited[n] = 1           # 시작점 방문 표시
    print(n)                 # do[n]
    while True:
        for w in range(1, V+1):    # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)  # push(n), v = w
                n = w
                print(n)         # do(w)
                visited[n] = 1   # w 방문 표시
                break            # for w, n에 인접인 w c찾은 경우

        else:
            if stack:# 스택에 지나온 정점이 남아있으면
                n = stack.pop()  # pop()해서 다시 다른 w를 찾을 n 찾기
            else:    # 스택이 비어있으면
                break  # while True 탐색 끝
    return

V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_m = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

dfs(1, V, adj_m)
'''


def dfs(start):
    # 차례대로 방문
    for w in gp[start]:
        # 방문하지 않았을 경우만
        if not visited[w]:
            dfs(w)



n, m, r = map(int, input().split())
# 그래프 초기화
gp = [[] for _ in range(n+1)]
# 방문체크용
visited = [0] * (n+1)

# 그래프 노드 연결
for _ in range(m):
    u, v = map(int, input().split())
    gp[u].append(v)
    gp[v].append(u)

# 오름차순으로 정렬
for i in range(n+1):
    gp[i].sort()


dfs(r)

for i in range(1, n+1):
    print(visited[i])