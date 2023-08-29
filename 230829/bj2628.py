col, row = map(int, input().split())
cnt_cut = int(input())
info_cut = [[], []]
for _ in range(cnt_cut):
    i, j = map(int, input().split())
    info_cut[i].append(j)

row_info = [row]
for i in info_cut[0]:
    row_info += [i]
col_info = [col]
for i in info_cut[1]:
    col_info += [i]

row_info.sort()
col_info.sort()

row, col = 0, 0

max_v1 = 0
for i in range(len(row_info)):
    if max_v1 < row_info[i] - row:
        max_v1 = row_info[i] - row
    row = row_info[i]

max_v2 = 0
for i in range(len(col_info)):
    if max_v2 < col_info[i] - col:
        max_v2 = col_info[i] - col
    col = col_info[i]

print(max_v1 * max_v2)