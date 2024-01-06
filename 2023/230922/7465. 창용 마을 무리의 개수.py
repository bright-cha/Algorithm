# 대표자 찾기
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

# 두 집합 묶어버리기
def union(x, y):
    global cnt

    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    parents = [i for i in range(N)]

    # 간선 정보 입력
    edge = []
    for _ in range(M):
        f, t = map(int, input().split())
        edge.append((f - 1, t - 1))

    # 나중에 입력 된 간선 정보를 앞에 입력된 데이터에 적용이 안되기 때문에
    # 두 번 돌아서 후반 데이터를 앞에서도 적용할 수 있게 하기 위해 2번 돈다.
    for _ in range(2):
        for x, y in edge:
            # 간선 정보를 통해 집합
            union(x, y)

    print(f'#{tc}', len(set(parents)))