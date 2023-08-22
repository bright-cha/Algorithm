import sys
sys.stdin = open('input.txt')
##########################################
def postorder_traversal(idx):
    if idx < cnt_node + 1:
        postorder_traversal(ch1[idx])
        postorder_traversal(ch2[idx])
        if type(tree[idx]) == int:
            rst.append(tree[idx])
        else:
            a2 = rst.pop()
            a1 = rst.pop()
            if tree[idx] == '+':
                rst.append(a1 + a2)
            elif tree[idx] == '-':
                rst.append(a1 - a2)
            elif tree[idx] == '*':
                rst.append(a1 * a2)
            elif tree[idx] == '/':
                rst.append(a1 // a2)
    else:
        return

T = 10
for tc in range(1, T + 1):
    print(tc, '================')
    cnt_node = int(input())

    tree = [0]
    ch1 = [0] * (cnt_node + 1)
    ch2 = [0] * (cnt_node + 1)
    for _ in range(1, cnt_node + 1):
        i = list(input().split())
        if i[1] not in '/*-+':
            i = int(i[1])
            tree.append(i)
        else:
            tree.append(i[1])
            ch1[int(i[0])] = int(i[2])
            ch1[int(i[0])] = int(i[3])

    rst = []
    postorder_traversal(1)
    print(tree)