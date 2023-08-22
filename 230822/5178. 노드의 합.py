import sys
sys.stdin = open('input.txt')
##########################################
def binary_tree(node):
    # 구하고자 하는 노드가 존재하는 노드인 경우
    if node < cnt_node + 1:
        # 이진으로 나눠서 들어간다. 왼자식 오른자식
        binary_tree(2 * node)
        binary_tree(2 * node + 1)
        # 만약 해당 노드의 값이 0이라면 이전 자식 노드들 값을 더해 선언한다.
        if parents[node] == 0:
            parents[node] = parents[node * 2] + parents[node * 2 + 1]


T = int(input())
for tc in range(1, T + 1):
    # 노드의 개수, 리프 노드의 개수, 출력할 노드
    cnt_node, cnt_leap, want_node = map(int, input().split())

    # (최대 노드 개수 준비물)높이를 구한다.
    height = 0
    for i in range(cnt_node):
        if cnt_node < 2 ** i:
            height = i - 1
            break

    # 리프 노드 정보를 입력받고 대입한다.
    # 최대 노드의 개수는  2^(높이+1) - 1이지만, 이진 트리를 저장할 인덱스는 0을 생각해서 + 1을해준다.
    parents = [0] * (2 ** (height + 1) - 1 + 1)
    for _ in range(cnt_leap):
        p, c = map(int, input().split())
        parents[p] = c

    # 이진트리 함수를 통해 남은 노드의 값을 구한다.
    binary_tree(1)
    print(f'#{tc}', parents[want_node])