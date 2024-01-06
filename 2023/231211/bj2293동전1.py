import sys
sys.setrecursionlimit(10 ** 7)


def backtracking(v, lst):
    global count, record

    for i in range(n):
        if dp[v][i]:
            # 더해진 값
            new_v = v + value_n[i]
            lst[i] += 1

            # 기준보다 커진 경우
            if new_v > k:
                dp[v][i] = False
                continue
            # 기준과 같은 경우
            elif new_v == k and tuple(lst) not in record:
                count += 1
                record.append(tuple(lst))
                lst[i] -= 1
                continue

            backtracking(new_v, lst)
            lst[i] -= 1



n, k = map(int, input().split())
value_n = [int(input()) for _ in range(n)]

count = 0

dp = [[True for _ in range(n)] for _ in range(100 ** 2)]
record = []
backtracking(0, [0 for _ in range(n)])
print(record)
print(count)