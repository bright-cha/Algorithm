T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrics = [[0] * 10 for _ in range(10)]  # 바탕 행렬을 만든다.
    puple = 0
    for _ in range(N):  # 색칠 영역을 받고 칠하는 반복문
        paint = list(map(int, input().split()))

        for i in range(paint[0], paint[2] + 1):  # 색깔의 행 시작지점과 종료지점 + 1 을 받는다.
            for j in range(paint[1], paint[3] + 1):  # 색깔의 열 시작지점과 종료지점 + 1을 받는다.
                if matrics[i][j] == 0:  # 아무것도 칠해져 있지 않다면 칠한다.
                    matrics[i][j] = paint[-1]
                elif matrics[i][j] != paint[-1]:  # 무언가 칠해져 있지만 같은 색깔이 아니라면 덧칠한다.
                    matrics[i][j] += paint[-1]

    for i in matrics:  # 모든 행렬을 살피고 보라색인 경우 갯수를 샌다.
        for j in i:
            if j == 3:
                puple += 1

    print(f'#{tc} {puple}')