import sys
sys.stdin = open('input.txt')
##################################
T = int(input())
for tc in range(1, T + 1):
    X, Y = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(X)]

    # 최고 길이
    max_len = 0

    for i in range(X):
        # 행마다 횟수 초기화
        cnt_x = 0
        for j in range(Y):
            # 만약 구조물이 있다면 횟수 증가
            if matrix[i][j] == 1:
                cnt_x += 1
            # 빈 땅의 경우, 길이가 최고값이라면 변경
            # 횟수 초기화
            else:
                if max_len < cnt_x:
                    max_len = cnt_x
                cnt_x = 0
        # 다음 행을 가기전 최고 횟수인지 확인
        if max_len < cnt_x:
            max_len = cnt_x

    for i in range(Y):
        # 열마다 횟수 초기화
        cnt_y = 0
        for j in range(X):
            # 만약 구조물이 있다면 횟수 증가
            if matrix[j][i] == 1:
                cnt_y += 1

            # 빈 땅의 경우, 길이가 최고값이라면 변경
            # 횟수 초기화
            else:
                if max_len < cnt_y:
                    max_len = cnt_y
                cnt_y = 0
        # 다음 열을 가기전 최고 횟수인지 확인
        if max_len < cnt_y:
            max_len = cnt_y

    print(f'#{tc}', max_len)
