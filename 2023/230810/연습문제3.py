import sys
sys.stdin = open("input.txt")


def dfs(n, V, adj_m):
    stack = []
    visited = [0] * (V+1) # 방문하면 1로 변경
    print(n, end='')
    visited[n] = 1
    while True:
# 2)정점 v에 인접한 정점 중에서
        for w in range(1, V+1): # 모든 정점에 대해서
            # w : 방문가능한지 확인할 정점
            # n : 현재 정점
            if adj_m[n][w] == 1: # n과 w가 연결되어있고
                if visited[w] == 0: # w를 방문한적이 없으면
                    # 방문하지 않은 정점 w가 있으면,
                    # 정점 v를 스택에 push하고
                    stack.append(n) # 기존위치 stack에 추가
                    # 정점 w를 방문한다.
                    # 그리고 w를 v로 하여
                    n = w # w에 방문
                    print(n, end='')
                    visited[n] = 1 # 방문했다고 표시
                    # 다시 2)를 반복한다.
                    break
    # 방문하지 않은 정점이 없으면,
        else:
        # 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은
            if stack: # stack pop 하기 전에 항상 확인
        # 가장 마지막 방문 정점을 v로 하여 다시 2를) 반복한다.
                n = stack.pop()
            else:
    #3)  스택이 공백이 될 때 까지 2)를 반복한다.
                break # while True 반복문 종료
    return


V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

dfs(1, V, adj_m)