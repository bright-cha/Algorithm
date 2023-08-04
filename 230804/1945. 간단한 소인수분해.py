T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 지수를 구하기 위해 밑을 리스트로 모은다.
    prime_nums = [2, 3, 5, 7, 11]

    # 지수를 정리하여 담기 위한 리스트를 만든다.
    cnt = [0] * 5
    for prime in prime_nums:
        # 지수를 하나씩 꺼내어 더이상 나누어지지 떨어지지 않을때까지
        # 반복하며 미리 만들어둔 리스트 내 인덱스에 넣는다.
        while N % prime == 0:
            N //= prime
            cnt[prime_nums.index(prime)] += 1

    print(f'#{tc}', *cnt)