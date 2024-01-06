def backtracking(idx, len, lst):
    global max_v
    if idx == len:
        sum_v = sum(lst)
        if max_v < sum_v:
            max_v = sum_v
        return

    else:
        idx += 1
        for i in range(idx, len):




cnt_day, sum_day = map(int, input().split())
temperature = list(map(int, input().split()))

max_v = 0
temp = []
backtracking(-1, sum_day, temp)