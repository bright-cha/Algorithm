import sys
sys.stdin = open('input.txt')
#########################################
T = int(input())
for tc in range(1, T + 1):
    decimal = float(input())
    code = ''
    while decimal:
        num = (decimal * 2) // 1
        code += str(int(num))
        decimal = (decimal * 2) % 1

    if len(code) > 12:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc}', code)