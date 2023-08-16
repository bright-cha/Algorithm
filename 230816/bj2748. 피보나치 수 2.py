import sys
sys.stdin = open('input.txt')
######################################
N = int(input())
memo = [0] * (N+1)
memo[0] = 0
memo[1] = 1
for i in range(2, N+1):
    memo[i] = memo[i-2] + memo[i-1]
print(memo[N])
