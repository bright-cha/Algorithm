def change(idx, leng, cnt):
    if len(rst) == 567:
        print(1)
    global max_v
    if cnt < 1:
        temp = int(''.join(num))
        if temp not in rst:
            rst.append(temp)
    else:
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
               if i != j:
                    num[j], num[i] = num[i], num[j]
                    change(idx % leng + 1, leng, cnt - 1)
                    num[j], num[i] = num[i], num[j]


T = int(input())
for tc in range(1, T + 1):
    num, chance = map(int, input().split())
    num = list(str(num))
    max_v = 0
    rst = []
    change(0, len(num), chance)
    print(f'#{tc}', max(rst))