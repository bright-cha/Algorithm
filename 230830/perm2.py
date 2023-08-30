def f(i, N):
    if i == N:  # 순열 완성
        print(p)
        return
    else:  # p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:  # 아직 사용하지 않았다면
                p[i] = card[j]
                used[j] = 1
                f(i + 1, N)
                used[j] = 0


card = [1, 2, 3, 4, 5, 6]
used = [0] * 6  # 이미 사용한 카드인지 표시
p = [0] * 6
f(0, 6)