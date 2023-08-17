"""
#  재귀1
def f(i, N):   # 0..3
    if i == N:
        return
    else:
        B[i] = A[i]   # 0 동일
        f(i + 1, N)   # 1, 3

N = 3
A = [1,2,3]
B = [0] * N
f(0, N)
print(B)

[1, 2, 3]

# 부분집합 재귀
def f(i, N):
    if i == N:
        print(bit, end='')
        s = 0
        for j in range(N):
            if bit[j]:
                s += A[j]
                print(A[j], end=' ')
        print(f' : {s}')
        return bit
    else:
        bit[i] = 1
        f(i + 1, N)  # 1, 1, 1
        bit[i] = 0   # 0, 1, 1,
        f(i + 1, N)
###################################함수와 실행문 구분선
A = [1,2,3]
bit = [0] * 3
f(0, 3)

# 출력값
# [1, 1, 1]1 2 3  : 6
# [1, 1, 0]1 2  : 3
# [1, 0, 1]1 3  : 4
# [1, 0, 0]1  : 1
# [0, 1, 1]2 3  : 5
# [0, 1, 0]2  : 2
# [0, 0, 1]3  : 3
# [0, 0, 0] : 0
"""
"""2번째 풀이
# 부분집합의 합 재귀2
def f(i, N, s): # s: i-1 원소까지 부분집합의 합(포함된 원소의 합)
    if i == N:
        print(bit, end='')
        print(f' : {s}')
        return bit
    else:
        bit[i] = 1               # 부분집합에 A[i] 포함
        f(i + 1, N, s + A[i])
        bit[i] = 0               # 부분집합에 A[i] 빠짐
        f(i + 1, N, s)
##################################함수와 실행문 구분선
A = [1,2,3]
bit = [0] * 3
f(0, 3, 0)

# 부분집합의 합 연습문제
def f(i, N, s, t): # s: i-1 원소까지 부분집합의 합(포함된 원소의 합), t 찾으려는 합
    global cnt
    cnt += 1
    if s == t:     #
        print(bit)
        return
    elif i == N:
        return
    elif s > t:
        return
    else:
        bit[i] = 1               # 부분집합에 A[i] 포함
        f(i + 1, N, s + A[i], t)
        bit[i] = 0               # 부분집합에 A[i] 빠짐
        f(i + 1, N, s, t)

# 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는?
# N = 크기
N = 10
A = [i + 1 for i in range(N)]
bit = [0] * N
cnt = 0
f(0, N, 0, 55)    # t 가 10 인경우 cnt = 349 / 55인경우 2047
print(cnt)
"""
