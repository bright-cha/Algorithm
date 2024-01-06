import sys
sys.stdin = open("input.txt")
###########################################################
def dfs(n, v, adj_m, g):
    stack = []
    visited = [0] * (v + 1)
    visited[n] = 1
    while True:
        if n == g:
            return 1

        for w in range(1, v + 1):
            if adj_m[n][w] == 1:
                if visited[w] == 0:
                    stack.append(n)
                    visited[w] = 1
                    n = w
                    break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    adj_m = [[0] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        v1 = arr[i][0]
        v2 = arr[i][1]
        adj_m[v1][v2] = 1

    print(f'#{tc}', dfs(S, V, adj_m, G))
