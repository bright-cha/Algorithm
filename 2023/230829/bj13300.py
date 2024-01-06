cnt_std, max_cnt = map(int, input().split())
students = [[], []]
min_room = 0
for _ in range(cnt_std):
    s, y = map(int, input().split())
    students[s].append(y)

for i in range(2):
    students[i].sort()

for i in range(2):
    cnt_in_room = 0
    while students[i]:
        std = students[i].pop()
        cnt_in_room += 1
        while std in students[i]:
            students[i].pop()
            cnt_in_room += 1

        min_room += (cnt_in_room // max_cnt)
        if cnt_in_room % max_cnt:
            min_room += 1
        cnt_in_room = 0
print(min_room)