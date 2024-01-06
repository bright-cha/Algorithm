'''
3
6
8
15

'''
import sys
sys.stdin = open('input.txt')
####################################
def inorder_traversal(T):
    global num
    if T < N + 1:
        inorder_traversal(2*T)
        rst[T] = num
        num += 1
        inorder_traversal(2*T + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    E = N - 1
    arr = [i for i in range(1, N + 1)]
    rst = [0] * (N+1)
    num = 1
    inorder_traversal(1)
    print(f'#{tc}', rst[1], rst[N//2])