import sys
input = sys.stdin.readline

# 내 풀이
'''
def brute_force(idx, start):
    global min_v

    if idx == N // 2:
        link = list(set(i for i in range(N)) - set(start))

        link_ability, start_ability = 0, 0
        for i in range(idx):
            for j in range(idx):
                if i != j:
                    link_ability += matrix[link[i]][link[j]]
                    start_ability += matrix[start[i]][start[j]]

        min_v = min(min_v, abs(start_ability - link_ability))

    else:
        for i in range(start[-1] + 1, N):
            if visited[i]:
                visited[i] = 0
                brute_force(idx + 1, start + [i])
                visited[i] = 1


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [1] * N

min_v = float('Inf')
brute_force(1, [0])
print(min_v)
'''

# GPT 최적화화
'''
def brute_force(idx, start_team, link_team, start_ability, link_ability):
    global min_v
    if idx == N:
        if len(start_team) == len(link_team):
            min_v = min(min_v, abs(start_ability - link_ability))
        return

    if len(start_team) < N // 2:
        next_ability = sum([matrix[idx][i] + matrix[i][idx] for i in start_team])
        brute_force(idx + 1, start_team + [idx], link_team, start_ability + next_ability, link_ability)

    if len(link_team) < N // 2:
        next_ability = sum([matrix[idx][i] + matrix[i][idx] for i in link_team])
        brute_force(idx + 1, start_team, link_team + [idx], start_ability, link_ability + next_ability)


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

min_v = float('Inf')
brute_force(0, [], [], 0, 0)
print(min_v)
'''

# 어느 미친 사람
from itertools import combinations

N = int(sys.stdin.readline())

stat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sum_stat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))] # 대각선끼리 합
allstat = sum(sum_stat) // 2 # 모든 값 합의 절반
result = float('inf')
for l in combinations(sum_stat, N//2): # 대각선 합에서 뽑은 2개 중에서
    result = min(result, abs(allstat - sum(l))) # 모든 값의 절반 - 그 뽑은 2개 합의 차 = start팀 - link팀
print(result)