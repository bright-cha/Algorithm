'''
00000010001101
'''
arr = input().strip()
for i in range(7, len(arr) + 1, 7):
    byte = arr[i - 7:i]
    print(int(byte, 2))