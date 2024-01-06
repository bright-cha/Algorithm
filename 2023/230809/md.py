# 최소값 구하기
def min_(ite):
    min_v = 1e9
    for i in ite:
        if min_v > i:
            min_v = i
    return min_v

# 최대값 구하기
def max_(ite):
    max_v = -1e9
    for i in ite:
        if max_v < i:
            min_v = i
    return max_v

# 길이 구하기
def len_(ite):
    cnt = 0
    for _ in ite:
        cnt += 1
    return cnt

# 모두 더하기
def sum_(ite):
    rst = 0
    for i in ite:
        rst += i
    return rst

# 포함되어있는지
def in_(ite, key):
    rst = None
    for i in ite:
        if i == key:
            rst = key
    if rst == key:
        return True
    else:
        return False