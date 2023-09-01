def check(x, y, vlaue):
    global min_v
    if min_v < vlaue:
        return

    if x == size - 1 and y == size - 1:
        min_v = min(min_v, vlaue)
        return

    for di, dj in delta:
        ni, nj = x + di, y + dj
        if ni < size and nj < size:
            check(ni, nj, vlaue + matrix[ni][nj])


T = int(input())
for tc in range(1, T + 1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]

    delta = [(0, 1), (1, 0)]
    min_v = 1e9

    sum_v = matrix[0][0]
    check(0, 0, sum_v)

    print(f'#{tc}', min_v)