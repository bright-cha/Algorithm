import sys
sys.stdin = open('input.txt')
####################################
T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)
    p = [0] * (E + 2)
    for i in range(E):
        parents, child = arr[2*i], arr[2*i+1]
        if ch1[parents] == 0:
            ch1[parents] = child
        else:
            ch2[parents] = child
        p[child] = parents
    print(ch1, ch2, p)

    cnt = 0
    while p[N]:
        N = p[N]
        cnt += 1
    print(cnt)