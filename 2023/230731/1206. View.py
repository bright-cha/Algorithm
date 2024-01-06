for tc in range(1, 11):
    N = input()
    arr = list(map(int, input().split()))

    rst = 0
    for i in range(2, len(arr) - 2):
        i_arr = [arr[i + j] for j in range(-2, 3) if j != 0]

        if arr[i] - max(i_arr) > 0:
            rst += arr[i] - max(i_arr)

    print(f'#{tc} {rst}')