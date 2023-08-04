T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    rst = []

    di = [0, 0, 0, 1, -1]
    dj = [0, 1, -1, 0, 0]
    for i in range(N):
        for j in range(M):
            sum_flower = 0
            for k in range(5):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    sum_flower += matrix[ni][nj]
            rst.append(sum_flower)

    print(f'#{tc}', max(rst))
