def ncr(n, r, s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = a[i]
            ncr(n, r-1, i+1)
a = [1,2,3,4,5,6]
n = len(a)
r = 2
comb = [0] * r
ncr(n, r, 0)