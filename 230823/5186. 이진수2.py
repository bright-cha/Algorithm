import sys
sys.stdin = open('input.txt')
#########################################
T = int(input())
for tc in range(1, T + 1):
    N = input().split('.')
    print(bin(N[-1], 10))