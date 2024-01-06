a = [1, 2, 3, 4]
N = 4

for i in range(1, 1 << N-1):  # 1 << N-1 == (1 << N) // 2
    subset1 = []
    subset2 = []
    total1 = 0
    total2 = 0
    for j in range(N):
        if i & (1 << j):  # j번 비트가 0이 아니면
            subset1.append(a[j])
            total1 += a[j]
        else:
            subset2.append(a[j])
            total2 += a[j]

    # r1 = f(subset1)
    # r2 = f(subset2)
    # if r1 and r2:
    #     if min_v > abs(total1 - total2):
    # print(subset1, subset2)

