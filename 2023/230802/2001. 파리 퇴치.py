T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrics = [list(map(int, input().split())) for _ in range(N)]

    di = []  # 델타 준비물
    dj = []
    for i in range(M):  # 파리채의 크기는 다양하고, 가로 세로가 M 인경우 넓이는 M * M
        for j in range(M - 1, -1, -1):
            di.append(i)
            dj.append(j)

    kill_nums = []  # 죽인 수
    for i in range(N):
        for j in range(N):
            rst = 0
            for k in range(M ** 2):  # 파리채 인덱스 하나씩 살피기 위해 M**2
                ni = i + di[k]
                nj = j + dj[k]
                if ni < N and nj < N:  # 0보다 작아지는 경우는 없지만, 행렬의 크기를 넘어갈 수 있기 때문에 N보다 작을 때만
                    rst += matrics[ni][nj]  # 각 인덱스 별로 잡은 수를 더한다.
            kill_nums.append(rst)  # 파리채로 한 번에 잡은 수를 리스트에 넣는다.

    best_kill = 0  # 최대값을 구한다.
    for i in kill_nums:
        if best_kill < i:
            best_kill = i

    print(f'#{tc} {best_kill}')