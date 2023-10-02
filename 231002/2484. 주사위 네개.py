import sys
input = sys.stdin.readline

N = int(input())
rst = [list(map(int, input().split())) for _ in range(N)]

ans = []
for i in rst:
    leng = len(set(i))
    if leng == 1:
        ans.append(50000 + 5000 * i[0])
        continue
    elif leng == 4:
        ans.append(100 * max(i))
        continue
    elif leng == 2:
        ans.append(2000 + sum(set(i)) * 500)

    temp = {}
    for j in i:
        temp.setdefault(j, 0)
        temp[j] += 1

    temp = list(map(lambda x: (x, temp[x]), temp))
    temp.sort(key=lambda x: x[1])

    if temp[-1][1] == 3:
        ans.append(10000 + temp[-1][0] * 1000)
    else:
        ans.append(1000 + temp[-1][0] * 100)

print(max(ans))