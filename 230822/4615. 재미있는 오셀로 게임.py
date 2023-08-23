import sys
sys.stdin = open('input.txt')
##########################################
def check_row(x, y, color):
    # 다음 지역 설정
    nx_plus = x + 1
    nx_minus = x - 1

    # 현재 탐색 지역이 다른 색인 경우 탐색지역리스트에 추가
    if board[x][y] != color and board[x][y] != 0:
        check_local.append((x, y))
    # 현재 탐색지역이 같은 색인 경우 탐색 했던 다른 색 변경
    elif board[x][y] == color:
        for i, j in check_local:
            board[i][j] = color
        check_local.clear()
        return

    # 만약 다음 지역이 이동가능하면 재귀
    if 0 <= nx_plus < len_side:
        check_row(nx_plus, y, color)
    # 아니라면 local 초기화
    else:
        check_local.clear()

    # 만약 다음 지역이 이동가능하면 재귀
    if 0 <= nx_minus < len_side:
        check_row(nx_minus, y, color)
    # 아니라면 local 초기화
    else:
        check_local.clear()

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
        check_local = []
        check_row(row-1, col-1, color)
        board[row][col] = color