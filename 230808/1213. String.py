import sys
sys.stdin = open("input.txt", "r")
#########################################


def brute_force(p, t):
        i = 0
        j = 0
        cnt = 0
        while i < N:
            if p[j] != t[i]:
                i = i - j
                j = -1
            i += 1
            j += 1
            if j == M:
                cnt += 1
                j = 0
        return cnt


for _ in range(10):
    tc = input()
    str1 = input()
    str2 = input()

    M = len(str1)
    N = len(str2)

    print(f'#{tc}', brute_force(str1, str2))
