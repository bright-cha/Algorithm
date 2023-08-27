cnt_fruit = int(input())
area = [[] for _ in range(5)]
sequence = []
for _ in range(6):
    i, y = map(int, input().split())
    if i not in sequence:
        sequence.append(i)
    area[i].append(y)


stack1 = []
stack2 = []
for i in sequence:
    now = area[i]
    if len(now) == 1:
        stack1.append(*now)
    elif len(now) == 2:
        if stack2:
            stack2.append(now[0])
        else:
            stack2.append(now[1])

rst = stack1[0] * stack1[1] - stack2[0] * stack2[1]
print(rst*cnt_fruit)

