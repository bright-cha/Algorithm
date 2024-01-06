N, M = map(int, input().split())
matrix = [[0] * M for _ in range(N)]

cnt = 0
q = [(0, 0)]
while q:
    cnt += 1
    i, j = q.pop(0)

    delta = [(i + 2, j + 1), (i + 1, j + 2), (i - 1, j + 2), (i - 2, j + 1)]
    if 0 <= i < N and 0 <= j < M:
        q.append((i, j))

print(cnt)