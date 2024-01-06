import sys
sys.stdin = open('input.txt')
###############################


def bfs(s, g):  # 출발지와 도착지
    q.append(s)                # 인큐
    visited[s] = 1             # 방문기록
    while q:                   # 큐에 정점이 남아 있으면
        t = q.pop(0)           # 디큐
        if t == g:
            return visited[t]
        for w in e_info[t]:    # 인점 정점 구하고
            if visited[w] == 0:  # 방문기록 없다면
                q.append(w)    # 인큐
                visited[w] = visited[t] + 1  # 방문 기록
    return 1

T = int(input().strip())
for tc in range(1, T + 1):
    V, E = map(int, input().strip().split())
    e_info = [[] for _ in range(V+1)]
    for _ in range(E):
        i, v = map(int, input().strip().split())
        e_info[i].append(v)
        e_info[v].append(i)
    S, G = map(int, input().split())
    visited = [0] * (V + 1)    # 방문기록지 생성
    q = []                 # 큐생성

    print(f'#{tc}', bfs(S, G) - 1)