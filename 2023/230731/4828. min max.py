T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    rst = 0

    for j in range(N - 1, -1, -1):
        for i in range(N - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    print(f'#{test_case} {arr[-1] - arr[0]}')
