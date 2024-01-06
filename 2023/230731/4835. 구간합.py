T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))


    sum_arr = []
    for i in range(len(arr) - (M-1)):
        sum_arr.append(sum(arr[i:i+M]))

    for i in range(len(sum_arr) - 1, -1, -1):
        for j in range(i):
            if sum_arr[j] > sum_arr[j+1]:
                sum_arr[j], sum_arr[j+1] = sum_arr[j+1], sum_arr[j]

    print(f'#{tc} {sum_arr[-1] - sum_arr[0]}')