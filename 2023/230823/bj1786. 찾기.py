def kmp(t, p):
    t_len = len(t)
    p_len = len(p)
    lps = [0] * (p_len + 1)
    # preprocessing
    j = 0                   # 일치한 개수 == 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, p_len):
        lps[i] = j          # p[i] 이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[p_len] = j


    cnt = 0
    # search
    i = 0                                # 비교할 텍스트 위치
    j = 0                                # 비교할 패턴 위치
    while i < t_len and j <= p_len:
        if j == -1 or t[i] == p[j]:      # 첫글자가 불일치했거나, 일치하면
            i += 1
            j += 1
        else:                            # 불일치
            j = lps[j]
        if j == p_len:                       # 패턴을 찾을 경우
            cnt += 1
            rst2.append(i - p_len+1)          # 패턴의 인덱스 출력
            j = lps[j]

    print()
    print(cnt)

T = input()
P = input()
rst2 = []
kmp(T, P)

print(''.join(map(str, rst2)))
