import sys
sys.stdin = open('input.txt')
#########################################
hex_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
           '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100',
           'D': '1101', 'E': '1110', 'F': '1111'}

bin_int = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
           '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for tc in range(1, T + 1):
    row, col = map(int, input().split())
    matrix = [input() for _ in range(row)]

    # 0만 있는 행 삭제
    zero = matrix[0]
    while zero in matrix:
        matrix.remove(zero)
    row = len(matrix)

    # 16진수 2진수로 변경
    for i in range(row):
        new_code = ''
        for j in range(col):
            new_code += hex_bin[matrix[i][j]]
        matrix[i] = new_code

    # 1을 만나는 경우 직전 0의 인덱스부터 끝까지로 수정
    code_candidates = [[]] * (row + 1)

    for i in range(row):
        local_1 = matrix[i].index('1') - 1
        matrix[i] = matrix[i][local_1:]

    for i in range(row):
        code = ''
        # 변화된 길이에 따른 새로운 열 확인
        col = len(matrix[i])
        for k in range(0, col, 7):
            if len(code) == 8:
                break
            while len(code) < 8:
                if matrix[i][k:k + 7] in bin_int:
                    num = bin_int[matrix[i][k:k + 7]]
                    code += str(num)
                    break

                else:
                    if len(code) == 0:
                        zero_cnt = 0
                        start_dict = {'01101': 0, '011001': 1, '010011': 2, '01011': 9}
                        first = matrix[i][:7]
                        while len(first) > 4:
                            if first in start_dict:
                                num = start_dict[first]
                                code += str(num)
                                while zero_cnt:
                                    matrix[i] = '0' + matrix[i]
                                    matrix[i] = matrix[i][:col]
                                    zero_cnt -= 1
                                break
                            else:
                                zero_cnt += 1
                                first = list(first)
                                first.pop()
                                first = ''.join(first)
                        if len(code) == 1:
                            break
                    matrix[i] = matrix[i].replace('00', '0')
                    matrix[i] = matrix[i].replace('11', '1')
        matrix[i] = code

    rst = 0
    for i in range(len(matrix)):
        matrix[i] = list(matrix[i])
        for j in range(8):
            matrix[i][j] = int(matrix[i][j])

        sum_v = (matrix[i][0] + matrix[i][2] + matrix[i][4] + matrix[i][6]) * 3 + (
                    matrix[i][1] + matrix[i][3] + matrix[i][5] + matrix[i][7])
        if sum_v % 10 == 0:
            rst = sum(matrix[i])

    print(f'#{tc}', rst)