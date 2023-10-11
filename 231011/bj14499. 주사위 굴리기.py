# 주사위 반대면은 7 - i
# x, y = 놓여진 위치 / 맨 처음 주사위 모든 면 = 0
N, M, x, y, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
info_k = list(map(int, input().split()))
dice = [0] * 7
dice_b = 6
dice_e = 3
dice_f = 2

for i in info_k:
    delta = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]
    dx, dy = delta[i]
    # matirx 상 위치 변화 적용
    nx, ny = x + dx, y + dy

    if not(0 <= nx < N and 0 <= ny < M):
        continue

    # 주사위 위치 변경
    if i == 1:
        dice_b, dice_e = dice_e, 7 - dice_b
    elif i == 2:
        dice_b, dice_e = 7 - dice_e, dice_b
    elif i == 3:
        dice_b, dice_f = dice_f, 7 - dice_b
    else:
        dice_b, dice_f = 7 - dice_f, dice_b



    # 0인 경우
    if matrix[nx][ny] == 0:
        matrix[nx][ny] = dice[dice_b]
    else:
        dice[dice_b] = matrix[nx][ny]
        matrix[nx][ny] = 0

    print(dice[7 - dice_b])

    x, y = nx, ny