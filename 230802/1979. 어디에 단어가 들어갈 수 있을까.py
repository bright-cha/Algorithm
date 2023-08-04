T = int(input())
for tc in range(1, T + 1):
    width, string = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(width)]

    rst = 0
    for i in range(width):
        straight = 0
        for j in range(width):
            if arr[i][j] == 1:
                straight += 1
            if arr[i][j] == 0 or j == width - 1:
                if straight == string:
                    rst += 1
                straight = 0

    for i in range(width):
        straight = 0
        for j in range(width):
            if arr[j][i] == 1:
                straight += 1
            if arr[j][i] == 0 or j == width - 1:
                if straight == string:
                    rst += 1
                straight = 0

    print(f'#{tc} {rst}')