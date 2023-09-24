import sys
input = sys.stdin.readline


def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


V, E = map(int, input().split())
parents = [i for i in range(V + 1)]
for _ in range(E):
    i, j = map(int, input().split())
    union(i, j)

# conunt가 돌때마다 모든 집합을 확인하다보니 시간초과 발생
# rst = 1
# for i in set(parents[1:]):
#     rst *= parents.count(i)

# 이러한 방식으로 집합을 한번만 확인할 수 있도록 한다.
temp = {}
for i in range(1, V + 1):
     j = find_set(i)
     temp[j] = temp.get(j, 0) + 1

rst = 1
for i in temp.values():
    rst *= i
    rst %= 1000000007

print(rst % 1000000007)