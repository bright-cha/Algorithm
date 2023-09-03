row, col = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]
cnt = 0

didj = []
for i in range(-1, 2, 1):
    for j in range(-1, 2, 1):
        if i == 0 and j == 0:
            continue
        didj.append((i, j))


visited = []
for i in range(row):
    for j in range(col):
        temp_visited = []
        ij = []
        flag = 0
        for di, dj in didj:
            ni, nj = i + di, j + dj
            if 0 <= ni < row and 0 <= nj < col:
                if matrix[i][j] < matrix[ni][nj]:
                    break
                if matrix[i][j] == matrix[ni][nj]:
                    temp_visited.append((i, j))
                    flag = 1
                    visited.append((i, j))
                    ij.append((ni, nj))
        else:
            while flag and ij:
                p, q = ij.pop(0)
                for di, dj in didj:
                    ni, nj = p + di, q + dj
                    if 0 <= ni < row and 0 <= nj < col:
                        if matrix[p][q] < matrix[ni][nj]:
                            flag = 0
                            visited.clear()
                            break
                        if matrix[p][q] == matrix[ni][nj] and ((ni, nj) not in temp_visited):
                            ij.append((ni, nj))
                            temp_visited.append((p, q))
            else:
                cnt += 1

print(cnt)
