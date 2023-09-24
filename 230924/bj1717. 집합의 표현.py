import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    elif x < y:
        parents[y] = x
    else:
        parents[x] = y


V, E = map(int, input().split())
parents = [i for i in range(V + 1)]
graph = []
for _ in range(E):
    v, a, b = map(int, input().split())
    if v == 0:
        union(a, b)
    else:
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')