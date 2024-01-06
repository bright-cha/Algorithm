import sys
sys.stdin = open('input.txt')
######################################3
T = int(input())
for tc in range(1, T + 1):
    # 행렬의 사이즈
    size = int(input())
    # 행렬 생성
    matrix = [list(input().split()) for _ in range(size)]

    # 테스트 케이스 출력
    print(f'#{tc}')
    # size 행 만큼 출력을 위해 반복
    for i in range(size):
        # 90도, 180도, 270도 문자열을 담기 위한 빈 문자열 생성
        # i 는 몇 번째 행을 뜻함
        str_90, str_180, str_270 = '', '', ''
        for j in range(size - 1, -1, -1):
            str_90 += matrix[j][i]

        for j in range(size - 1, -1, -1):
            str_180 += matrix[(size-1) - i][j]

        for j in range(size):
            str_270 += matrix[j][(size-1) - i]
        print(str_90, str_180, str_270)