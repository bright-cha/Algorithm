N, M = map(int, input().split())
matrix = [[j for j in range(i - M + 1, i + 1)] for i in range(M, N * M + 1, M)]

for i in matrix:
    print(*i)