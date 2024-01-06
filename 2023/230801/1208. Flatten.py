T = 10
for tc in range(1, T + 1):
    chance = int(input())
    box_heigh = list(map(int, input().split()))

    while chance != 0:
        for i in range(99, 0, -1):
            for j in range(i):
                if box_heigh[j] > box_heigh[j + 1]:
                    box_heigh[j], box_heigh[j + 1] = box_heigh[j + 1], box_heigh[j]

        box_heigh[-1] -= 1
        box_heigh[0] += 1
        chance -= 1

    for i in range(99, 0, - 1):
        for j in range(i):
            if box_heigh[j] > box_heigh[j + 1]:
                box_heigh[j], box_heigh[j + 1] = box_heigh[j + 1], box_heigh[j]

    print(f'#{tc} {box_heigh[-1] - box_heigh[0]}')