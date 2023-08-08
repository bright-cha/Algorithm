# 단어의 길이를 구하는 함수
def len_(word):
    cnt = 0
    for _ in word:
        cnt += 1
    return cnt


# 브루트 포스를 통해 패턴이 나오는 횟수 세기
def b_f(t, p):
    i = 0
    j = 0
    cnt = 0
    # 모든 문자를 검사할때까지 반복
    while i < len_str1:
        # 만약 해당 문자가 패턴 문자가 아니라면
        if t[i] != p[j]:
            # 검사할 문자 위치를 초기화
            i = i - j
            # 패턴의 문자 위치 초기화
            j = -1
        i += 1
        j += 1
        # 만약 패턴의 문자를 찾는다면 횟수 증가 및 패턴 문자 초기화
        if j == len_str2:
            cnt += 1
            j = 0
    return cnt


T = int(input())
for tc in range(1, T + 1):
    str1, str2 = input().split()
    len_str1 = len_(str1)
    len_str2 = len_(str2)

    # 패턴이 아닌 글자 수(총 문자 길이 - 패턴이 차지하는 길이) + 패턴 횟수
    rst = len_str1 - (len_str2 * b_f(str1, str2)) + b_f(str1, str2)
    print(f'#{tc}', rst)