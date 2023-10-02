N = str(input())
temp = 0
for i in range(len(N)):
    if i < len(N) - 1 and N[i + 1] == '0':
        temp += 10
    else:
        temp += int(N[i])

print(temp)