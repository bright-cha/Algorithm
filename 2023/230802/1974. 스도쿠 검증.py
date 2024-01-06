T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    rst = 1

    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[i][j]] += 1
        if 2 in cnt:
            rst = 0

    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[j][i]] += 1
        if 2 in cnt:
            rst = 0

    di = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    dj = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            cnt = [0] * 10
            for k in range(9):
                ni = i + di[k]
                nj = j + dj[k]
                cnt[arr[ni][nj]] += 1
            if 2 in cnt:
                rst = 0

    print(f'#{tc} {rst}')
