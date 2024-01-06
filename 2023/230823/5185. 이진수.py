converter = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
T = int(input())
for tc in range(1, T + 1):
    length, num = input().split()
    code = ''
    for idx in num:
        if idx in converter:
            idx = converter[idx]
        else:
            idx = int(idx)

        temp_code = ''
        for _ in range(4):
            temp = idx
            idx //= 2
            temp_code = str(temp % 2) + temp_code

        code += temp_code

    print(f'#{tc}', code)

