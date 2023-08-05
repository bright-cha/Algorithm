T = int(input())
for tc in range(1, T + 1):
    width = int(input())
    lines = list(map(int, input().split())) \
 \
            rst = []
    for line_ind in range(len(lines)):
        cnt = 0
        for line2_ind in range(line_ind + 1, len(lines)):
            if lines[line_ind] > lines[line2_ind]:
                cnt += 1
        rst.append(cnt)

    max_val = -1
    for num in rst:
        if max_val < num:
            max_val = num
    print(f'#{tc} {max_val}')