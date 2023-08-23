import sys
sys.stdin = open('input.txt')
####################################
def find_node_cnt(num):
    global cnt
    if ch1[num] != 0:
        cnt += 1
        find_node_cnt(ch1[num])
    if ch2[num] != 0:
        cnt += 1
        find_node_cnt(ch2[num])


T = int(input())
for tc in range(1, T + 1):
    cnt_edge, root_num = map(int, input().split())
    cnt_node = cnt_edge + 1
    ch1 = [0] * (cnt_node + 1)
    ch2 = [0] * (cnt_node + 1)
    info_edge = list(map(int, input().split()))

    for i in range(cnt_edge):
        parents, child = info_edge[i * 2], info_edge[i * 2 + 1]
        if ch1[parents] == 0:
            ch1[parents] = child
        else:
            ch2[parents] = child

    cnt = 1
    find_node_cnt(root_num)
    print(f'#{tc}', cnt)
