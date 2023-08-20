'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(s):
    q.append(s)
    visited[s] = 1
    while q:
        t = q.pop(0)
        print(t, end=' ')

        for i in gp[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1


V, street_cnt = map(int, input().split())
street = list(map(int, input().split()))

gp = [[] for _ in range(V + 1)]
for i in range(street_cnt):
    v1, v2 = street[i * 2], street[i * 2 + 1]
    gp[v1].append(v2)
    gp[v2].append(v1)

visited = [0] * (V + 1)
q = []

bfs(1)