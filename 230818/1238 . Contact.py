import sys
sys.stdin = open('input.txt')
##############################
def bfs(start):
    q.append(start)
    visited[start] = 1
    while q:
        t = q.pop(0)
        for i in grape[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1


for tc in range(1, 11):
    len_data, start = map(int, input().split())
    from_to = list(map(int, input().split()))
    grape = [[] for _ in range(101)]
    for i in range(len_data//2):
        v1, v2 = from_to[i * 2], from_to[i*2 + 1]
        grape[v1].append(v2)
    visited = [0] * 101
    q = []

    bfs(start)
    visited.reverse()
    max_v = max(visited)
    print(f'#{tc}', 100 - visited.index(max_v))