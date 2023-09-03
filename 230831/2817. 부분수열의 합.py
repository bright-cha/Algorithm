T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = 0
    for i in range(1, 1 << len(A)):
        temp = 0
        for j in range(len(A)):
            if i & (1 << j):
                temp += A[j]
                if temp > K:
                    break
        if temp == K:
            cnt += 1

    print(f'#{tc}', cnt)