import sys
sys.stdin = open('input.txt')
##########################################
def traversal(idx):
    if idx <= cnt_node:
        if ch1[idx]:
            traversal(ch1[idx])
            traversal(ch2[idx])
        stack.append(tree[idx])


for tc in range(1, 11):
    cnt_node = int(input())
    tree = [0] * (cnt_node + 1)
    ch1 = [0] * (cnt_node + 1)
    ch2 = [0] * (cnt_node + 1)
    stack = []
    for _ in range(1, cnt_node + 1):
        i = list(input().split())
        if i[1] not in '/*-+':
            node, num = int(i[0]), i[1]
            tree[node] = num
        else:
            ch1[int(i[0])] = int(i[2])
            ch2[int(i[0])] = int(i[3])
            tree[int(i[0])] = i[1]

    traversal(1)

    rst = []
    for i in stack:
        if i not in '/*-+':
            i = int(i)
            rst.append(i)
        else:
            a2 = rst.pop()
            a1 = rst.pop()
            if i == '+':
                rst.append(a1 + a2)
            if i == '-':
                rst.append(a1 - a2)
            if i == '*':
                rst.append(a1 * a2)
            if i == '/':
                rst.append(a1 / a2)

    print(f'#{tc}', int(*rst))