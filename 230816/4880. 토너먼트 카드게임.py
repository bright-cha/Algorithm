import sys
sys.stdin = open('input.txt')
#######################################
def winner(start, end):
    # 사람의 수
    n = end - start + 1

    # 1명인 경우
    if n == 1:
        return start
    else:  # 2명 이상인 경우 2그룹으로 나눈다.
        p = (start + end) // 2
        w1 = winner(start, p)
        w2 = winner(p + 1, end)

    p1 = card[w1]
    p2 = card[w2]
    if (p1, p2) == (3, 1) or (p1, p2) == (1, 2) or (p1, p2) == (2, 3):
        return w2
    else:
        return w1


T = int(input())
for tc in range(1, T + 1):
    people = int(input())
    card = list(map(int, input().split()))

    print(f'#{tc}', winner(0, people-1) + 1)