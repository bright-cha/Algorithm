R, C, ZR, ZC = map(int, input().split())
news = [list(input()) if i % ZR == 0 else [] for i in range(R * ZR)]

for i in range(R * ZR):
    for j in range(C):
        if i % ZR != 0:
            news[i] = news[i - 1]
        else:
            news[i][j] *= ZC

for i in news:
    print(''.join(i))