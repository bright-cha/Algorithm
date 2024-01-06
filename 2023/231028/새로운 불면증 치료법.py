for tc in range(1, int(input()) + 1):
    N = int(input())
    record = [0] * 10

    idx = 1
    while 0 in record:
        temp = N * idx
        while temp > 0:
            digit = temp % 10
            record[digit] = 1
            temp //= 10
        idx += 1

    print(f'#{tc}', (idx - 1) * N)