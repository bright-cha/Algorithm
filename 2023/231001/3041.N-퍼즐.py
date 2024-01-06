matrix = [list(input()) for _ in range(4)]
ans = ['ABCD',
      'EFGH' ,
      'IJKL' ,
      'MNO.']

temp = 0
for i in range(4):
    for j in range(4):
        if ans[i][j] == '.':
            continue
        if matrix[i][j] != ans[i][j]:
            flag = True
            for a in range(4):
                if flag:
                    for b in range(4):
                        if matrix[a][b] == ans[i][j]:
                            temp += abs(i - a) + abs(j - b)
                            flag = False
                            break

print(temp)