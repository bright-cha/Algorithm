import sys
input = sys.stdin.readline

word = input().rstrip()
temp = ['M', 'O', 'B', 'I', 'S']
ans = 0
for i in temp:
    if i in word:
        ans += 1

if ans == 5:
    print('YES')
else:
    print('NO')
