def change(idx, leng, cnt):
    global max_v
    if cnt < 1:
        temp = int(''.join(num))
        if temp not in rst:
            rst.append(temp)
    else:
        for i in range(len(num)):
            if i != idx % leng:
                num[idx % leng], num[i] = num[i], num[idx % leng]
                change(idx % leng + 1, leng, cnt - 1)
                num[idx % leng], num[i] = num[i], num[idx % leng]


T = int(input())
for tc in range(1, T + 1):
    num, chance = map(int, input().split())
    num = list(str(num))
    max_v = 0
    rst = []
    change(0, len(num), chance)
    print(f'#{tc}', max(rst))