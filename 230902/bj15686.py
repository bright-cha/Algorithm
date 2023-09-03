def chack_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


size, max_store = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(size)]

# 집과 가게 위치 찾아 저장
local_store = []
local_house = []
for i in range(size):
    for j in range(size):
        if matrix[i][j] == 2:
            local_store.append([(i, j)])
        elif matrix[i][j] == 1:
            local_house.append((i, j))

# 만약 치킨집의 개수가 많다면 각 치킨집별로 치킨거리 파악하기
if len(local_store) > max_store:
    # 제거 해야하는 가게 파악
    delete = len(local_store) - max_store

    # 각 가게 별로 없을 때, 치킨거리 파악하기
    for _ in range(len(local_store)):
        rst = 0
        i, j = local_store.pop(0)[0]
        for house in local_house:
            temp = 10000000000
            for store in local_store:
                x, y = store[0]
                distance = chack_distance(x, y, house[0], house[1])
                temp = min(distance, temp)
            rst += temp
        local_store.append([(i, j), rst])
    print(local_store)
    local_store.sort(key=lambda x: x[1], reverse=True)

    for _ in range(delete):
        i, j = local_store.pop()[0]
        # 지도에서 지우기
        matrix[i][j] = 0

# 각 집별로 치킨 거리를 구해서 저장한다.
rst = 0
for house in local_house:
    temp = 10000000000
    for store in local_store:
        x, y = store[0]
        distance = chack_distance(x, y, house[0], house[1])
        temp = min(distance, temp)
    rst += temp

print(rst)