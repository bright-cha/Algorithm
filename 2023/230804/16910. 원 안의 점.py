T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    cnt = 0  # 결과값
    '''
    # 만약 반지름이 1인 경우,
    # 격자점은 (0, 0)(1, 0)(0, 1)(-1, 0)(1, 0)
    # 즉, X와 Y가 -1 ~ 1 까지의 조합으로 이루어지게 된다.
    # 따라서 i와 j의 부호를 다르게 작성하고 문제에서 주어진
    # 공식이 적용되는 경우를 구하면 된다
    '''
    for i in range(-N, N + 1):
        for j in range(N, -N - 1, -1):
            if i ** 2 + j ** 2 <= N ** 2:
                cnt += 1

    print(f'#{tc} {cnt}')