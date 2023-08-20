import sys
sys.stdin = open('bj15489.txt')
####################################
def pascal(r, w):
    for i in range(r+w):
        triangle.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                triangle[i].append(1)
            else:
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])


r, c, w = map(int, input().split())
triangle = []
pascal(r, w)
sum_v = 0
for i in range(r-1, r+w-1):
    for j in range(c-1, i-r+c+1):
        sum_v += triangle[i][j]
print(sum_v)

