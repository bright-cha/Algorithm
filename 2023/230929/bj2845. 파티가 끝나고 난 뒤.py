P, G = map(int, input().split())
lst = list(map(int, input().split()))

ap = P * G
for i in lst:
    print(i - ap, end=' ')