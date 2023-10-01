import sys
input = sys.stdin.readline


N = int(input())
size = 5 * N
matrix = []
for _ in range(N):
    temp = [list(input()) for _ in range(5)]
    matrix.append(temp)

min_v = [1e9, -1, -1]
for i in range(N):
    for j in range(N):
        if i == j:
            continue

        temp = 0
        for a in range(5):
            if min_v[0] <= temp:
                break
            for b in range(7):
                if min_v[0] <= temp:
                    break
                if matrix[i][a][b] != matrix[j][a][b]:
                    temp += 1

        if min_v[0] > temp:
            if i > j:
                min_v = [temp, j, i]
            else:
                min_v = [temp, i, j]

print(min_v[1] + 1, min_v[2] + 1)