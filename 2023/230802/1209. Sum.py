T = 10
for tc in range(1, T + 1):
    N = int(input())
    matrics = [list(map(int, input().split())) for _ in range(100)]

    line_sum = []

    for i in matrics:
        sum = 0
        for j in i:
            sum += j
        line_sum.append(sum)

    for i in range(100):
        sum = 0
        for j in range(100):
            sum += matrics[j][i]
        line_sum.append(sum)

    sum = 0
    for i in range(100):
        sum += matrics[i][i]
    line_sum.append(sum)

    sum = 0
    for i in range(100):
        sum += matrics[i][-(i + 1)]
    line_sum.append(sum)

    max_v = 0
    for i in line_sum:
        if max_v < i:
            max_v = i

    print(f'#{tc} {max_v}')