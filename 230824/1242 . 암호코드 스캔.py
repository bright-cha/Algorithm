import sys
sys.stdin = open('input.txt')
#########################################
hex_num = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
           '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100',
           'D': '1101', 'E': '1110', 'F': '1111'}

int_num = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
           '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for tc in range(1, T + 1):
    row, col = map(int, input().split())
    matrix = [input() for _ in range(row)]
    for i in range(row):
        new_code = ''
        for j in range(col):
            new_code += hex_num[matrix[i][j]]
        matrix[i] = new_code

    for i in matrix:
        idx = 0
        for j in i:
            if j == '1':
                idx -= 1
                break
            else:
                idx += 1
        new_code = ''
        flag = 1
        while flag and idx != col * 4:
            for k in range(idx, col * 4, 7):
                if len(i) < 7:
                    break
                if i[k:k+7] in int_num:
                    print(i[k:k+7])
                    flag = 0
                else:
                    i = i.replace('00', '0')
                    i = i.replace('11', '1')
                    idx = idx // 2

                # new_code =
