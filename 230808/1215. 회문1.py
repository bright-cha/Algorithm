import sys
sys.stdin = open("input.txt", "r")
#########################################
T = 10
for tc in range(1, T + 1):
    length = int(input())
    matrix = [list(input()) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(8 - length + 1):
            # 행 순회
            check_word = ''
            for k in range(length // 2):
                if matrix[i][j + k] != matrix[i][j + length - 1 - k]:
                    break
            else:
                cnt += 1

            # 열 순회
            check_word = ''
            for k in range(length // 2):
                if matrix[j + k][i] != matrix[j + length - 1 - k][i]:
                    break
            else:
                cnt += 1

    print(f'#{tc}', cnt)