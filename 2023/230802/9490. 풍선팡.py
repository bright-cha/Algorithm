T = int(input())
for tc in range(1, T + 1):
    width, length = map(int, input().split())  # 가로 세로
    flower = [list(map(int, input().split())) for _ in range(width)]  # 꽃가루

    # 중심 구하기
    rst = []
    for i in range(width):
        for j in range(length):

            mid = flower[i][j]

            # 중심의 di dj구하기
            di = []
            dj = []
            for a in range(-mid, mid + 1):  # 중심값만큼 위아래 인덱스 번호
                for b in range(mid, -mid - 1, -1):
                    if a == 0 or b == 0:  # 가로 세로 중 하나가 0이어야 한다.
                        di.append(a)
                        dj.append(b)

            # 중심과 di dj를 활용하여 ni nj를 구하고 각 인덱스를 더한다.
            sum_flower = 0
            for k in range(len(di)):  #
                # print(f'a = {a} b = {b} k = {k} {flower[a][b]}')
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < width and 0 <= nj < length:
                    sum_flower += flower[ni][nj]

            rst.append(sum_flower)

    max_rst = 0
    for i in rst:
        if max_rst < i:
            max_rst = i

    print(f"#{tc} {max_rst}")