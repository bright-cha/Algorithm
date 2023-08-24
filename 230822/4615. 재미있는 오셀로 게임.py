import sys
sys.stdin = open('input.txt')
##########################################
def check_around(row, col, me):
    local = []

    di = [0, 0, 0, 1, 1, 1, -1, -1, -1]
    dj = [0, 1, -1, 0, 1, -1, 0, 1, -1]
    for k in range(9):
        ni = row + di[k]
        nj = col + dj[k]
        while 0 <= ni < len_side and 0 <= nj < len_side and board[ni][nj] != 0:
            if board[ni][nj] == me:
                break
            else:  # 너인 경우
                local.append((ni, nj))
            ni += di[k]
            nj += dj[k]
        else:
            local.clear()

        if local:
            for i, j in local:
                board[i][j] = me


T = int(input())
for tc in range(1, T + 1):
    len_side, cnt_put = map(int, input().split())
    colors = [list(map(int, input().split())) for _ in range(cnt_put)]

    board = [[0] * len_side for _ in range(len_side)]
    board[len_side // 2 - 1][len_side // 2 - 1] = 2
    board[len_side // 2][len_side // 2] = 2
    board[len_side // 2][len_side // 2 - 1] = 1
    board[len_side // 2 - 1][len_side // 2] = 1

    for col, row, color in colors:
        row -= 1
        col -= 1
        board[row][col] = color
        check_around(row, col, color)

    b, w = 0, 0
    for i in range(len_side):
        for j in range(len_side):
            if board[i][j] == 1:
                b += 1
            elif board[i][j] == 2:
                w += 1
    print(f'#{tc}', b, w)