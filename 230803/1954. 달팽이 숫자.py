T = int(input())
for tc in range(1, T + 1):
    # 달팽이 크기
    size = int(input())

    # 달팽이 행렬 기본값 0
    snail = [[0] * size for _ in range(size)]
    nums = [i for i in range(1, size ** 2 + 1)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    direction = 0

    x = 0
    y = -1
    while len(nums):
        direction %= 4
        ni, nj = x + di[direction], y + dj[direction]
        if 0 <= ni < size and 0 <= nj < size:
            if snail[ni][nj] == 0:
                snail[ni][nj] = nums.pop(0)
                x = ni
                y = nj
            else:
                direction += 1
        else:
            direction += 1

    print(f'#{tc}')
    for i in snail:
        print(*i)