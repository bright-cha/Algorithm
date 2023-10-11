import sys
input = sys.stdin.readline

def solve_distance(lst):
    global min_v

    distance = 0
    for i, j in house_info:
        temp = float('inf')
        for x, y in lst:
            dist = abs(x - i) + abs(y - j)
            temp = min(temp, dist)
        distance += temp

    min_v = min(min_v, distance)


def combination(idx, open):
    if len(open) > M:
        return

    if idx == cnt_chicken:
        if len(open) == M:
            solve_distance(open)
        return

    else:
        combination(idx + 1, open + [chicken_info[idx]])
        combination(idx + 1, open)


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

chicken_info = []
house_info = []
cnt_chicken = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            cnt_chicken += 1
            chicken_info.append((i, j))
        if matrix[i][j] == 1:
            house_info.append((i, j))

min_v = float('inf')
visited = [0] * cnt_chicken
combination(0, [])
print(min_v)