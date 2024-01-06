T = int(input())
for tc in range(1, T + 1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]

    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    max_v = 0
    min_start = 0
    for i in range(size):
        for j in range(size):
            p, q = i, j
            cnt = 1
            while True:
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < size and 0 <= nj < size and matrix[i][j] + 1 == matrix[ni][nj]:
                        cnt += 1
                        i, j = ni, nj
                        break
                else:
                    break
            if max_v == cnt and min_start > matrix[p][q]:
                min_start = matrix[p][q]
            elif max_v < cnt:
                max_v = cnt
                min_start = matrix[p][q]

    print(f'#{tc}', min_start, max_v)