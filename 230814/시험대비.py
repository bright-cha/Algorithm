# import sys
# sys.stdin = open('input.txt')
##########################################
# 버블 정렬
'''
def bobule():
    lst = [5, 4, 2, 1, 3]
    N = len(lst)
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    print(lst)
'''
# 카운팅 정렬
'''
def counting():
    lst = [5, 4, 2, 1, 3]
    cnt = [0] * (max(lst) + 1)
    rst = [0] * len(lst)
    for i in range(len(lst)):
        cnt[lst[i]] += 1

    for i in range(1, len(cnt)):
        cnt[i] += cnt[i - 1]

    for i in range(len(lst) - 1, -1, -1):
        cnt[lst[i]] -= 1
        rst[cnt[lst[i]]] = lst[i]

    print(rst)
    '''
# 부분집합 생성
'''
def subset():
    lst = [0, 1, 2, 3, 4, 5]
    for i in range(1 << len(lst)):
        for j in range(len(lst)):
            if i & (1 << j):
                print(lst[j], end = '')
        print()
        '''
# 바이너리 서치 (이분탐색)
'''
def binary_search(lst, key, start, end):
    if start > end:
        return False
    else:
        middle = (start + end) // 2
        if lst[middle] == key:
            return True
        elif lst[middle] < key:
            return binary_search(lst, key, middle + 1, end)
        else:
            return binary_search(lst, key, start, middle - 1)


    lst = [0, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20]
    # s = 0
    # e = len(lst) - 1
    # k = 10
    # while s <= e:
    #     mid = (s + e) // 2
    #     if k == lst[mid]:
    #         print(1)
    #         break
    #     elif lst[mid] < k:
    #         s = mid + 1
    #     else:
    #         e = mid - 1
    # else:
    #     print(0)

    # print(binary_search(lst, 20, 0, len(lst)-1))
'''
# 선택정렬
'''
def selection_sort():
    lst = [1, 54, 89, 64,63, 4165, 4654, 654, 65, 41,56, 456, 4564, 56, 423, 4, 56, 4]
    for i in range(len(lst) - 1):
        min_v = i
        for j in range(i + 1, len(lst)):
            if lst[min_v] > lst[j]:
                min_v = j
        lst[i], lst[min_v] = lst[min_v], lst[i]
    print(lst)
selection_sort()
'''
# 셀렉션 알고리즘
'''
def selection_algorithm():
    lst = [1, 54, 89, 64, 63, 4165, 4654, 654, 65, 41, 56, 456, 4564, 56, 423, 4, 56, 4]
    k = 10
    for i in range(k):
        min_v = i
        for j in range(i + 1, len(lst)):
            if lst[min_v] > lst[j]:
                min_v = j
        lst[i], lst[min_v] = lst[min_v], lst[i]
    print(lst[k-1])
selection_algorithm()
'''
##########################################
# 문자열 - 브루트포스
'''
t = '1231231231234123'
p = '12345'
len_t = len(t)
len_p = len(p)

def BruteForce(p, t):
    i = 0
    j = 0
    while j < len_p and i < len_t:
        if t[i] != p[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == len_p:
        return True
    else:
        return False
print(BruteForce(p, t))
'''
##########################################
# 스택
# 재귀호출
'''
def fibo1(n):
    if n < 2:
        return n
    else:
        return fibo1(n - 1) + fibo1(n - 2)
print(fibo1(7))
'''
# DP
'''
def dp(n):
    fibo = [0] * (n + 1)
    fibo[1] = 1
    for i in range(2, n + 1):
        fibo[i] = fibo[i-1] + fibo[i - 2]
    print(fibo[n])
dp(7)
'''
##########################################
# DFS - 깊이 우선 탐색

'''입력값: 6 5 /n 1 4 1 3 2 3 2 5 4 6'''
'''
def dfs(n, V, adj_m):
    stack = []               # stack 생성
    visited = [0] * (V+1)    # visited 생성
    visited[n] = 1           # 시작점 방문 표시
    print(n)                 # do[n]
    while True:
        for w in range(1, V+1):    # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)  # push(n), v = w
                n = w
                print(n)         # do(w)
                visited[n] = 1   # w 방문 표시
                break            # for w, n에 인접인 w c찾은 경우

        else:
            if stack:# 스택에 지나온 정점이 남아있으면
                n = stack.pop()  # pop()해서 다시 다른 w를 찾을 n 찾기
            else:    # 스택이 비어있으면
                break  # while True 탐색 끝
    return

V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_m = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

dfs(1, V, adj_m)
'''  # while문

'''
def dfs(start):
    # 방문표시를 True 나 1 대신 방문순서로 대체
    visited[start] = 1
    # 차례대로 방문
    for w in adj_m[start]:
        # 방문하지 않았을 경우만
        if not visited[w]:
            dfs(w)

# 입력
n, m, r = map(int, input().split())

# 그래프 초기화
adj_m = [[] for _ in range(n+1)]

# 방문체크용
visited = [0] * (n+1)

# 그래프 노드 연결
for _ in range(m):
    u, v = map(int, input().split())
    adj_m[u].append(v)
    adj_m[v].append(u)

# 오름차순으로 정렬
for i in range(n+1):
    adj_m[i].sort()

# 탐색
dfs(r)
'''  # 재귀로 풀기