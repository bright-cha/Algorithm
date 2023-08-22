import sys
sys.stdin = open('input.txt')
##########################################


def enqueue(cnt_n):
    global last
    # 인덱스 1 증가
    last += 1
    # 부모는 자식의 2분의 1
    parents = last // 2
    # 트리 마지막 인덱스에 값 저장
    tree[last] = cnt_n
    #  자식 노드 선언
    child = last
    while parents:
        # 자식노드보다 부모노드가 크다면 둘을 바꾸고 자식 노드 번호를 부모노드번호로 갱신
        # 갱신된 자식 노드에 맞게 부모노드 번호 수정
        # 변화가 필요 없는 경우 반복문 종료
        if tree[parents] > tree[child]:
            tree[parents], tree[child] = tree[child], tree[parents]
            child = parents
            parents = child // 2
        else:
            break


T = int(input())
for tc in range(1, T + 1):
    cnt_node = int(input())
    nodes_value = list(map(int, input().split()))
    # 트리를 입력할 리스트 초기화
    tree = [0] * (cnt_node + 1)
    # 마지막 인덱스를 표시할 변수
    last = 0
    # 입력받은 값을 하나씩 엔큐
    for i in range(cnt_node):
        enqueue(nodes_value[i])

    # 값의 합을 담을 변수
    sum_v = 0
    while cnt_node:
        sum_v += tree[cnt_node // 2]
        cnt_node //= 2

    print(f'#{tc}', sum_v)
