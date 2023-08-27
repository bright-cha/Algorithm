cnt_fruit = int(input())
area = [[] for _ in range(5)]
sequence = [0]
for _ in range(6):
    i, y = map(int, input().split())
    sequence.append(i)
    area[i].append(y)

stack1 = []
stack2 = []
for i in range(1, len(sequence)):
    now = area[sequence[i]]
    if len(now) == 1:
        stack1.append(*now)
    else:
        if i == 1 and not stack1:
            pass


rst = stack1[0] * stack1[1] - stack2[0] * stack2[1]
print(rst*cnt_fruit)

'''
7
3 20
1 100
4 50
2 160
3 30
1 60


1
2 5
3 5
1 1
4 2
1 4
4 3

1
4 50
2 160
3 20
1 100
3 30
1 60
'''