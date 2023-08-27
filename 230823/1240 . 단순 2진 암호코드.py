bin_int = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
           '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
T = int(input())
for tc in range(1, T + 1):
    row, col = map(int, input().split())
    matrix = [list(input()) for _ in range(row)]

    # 1을 만나는 경우 직전 0의 인덱스부터 끝까지로 수정
    code_candidates = [0] * row
    for i in range(row):
        if '1' in matrix[i]:
            local_1 = matrix[i].index('1') - 1
            matrix[i] = matrix[i][local_1:]
        else:
            matrix[i] = []

    while [] in matrix:
        matrix.remove([])
    row = len(matrix)

    for i in range(row):
        code = ''
        # 변화된 길이에 따른 새로운 열 확인
        col = len(matrix[i])
        for k in range(0, col, 7):
            if len(code) == 8:
                break
            while len(code) < 8:
                temp = ''.join(matrix[i][k:k + 7])
                if temp in bin_int:
                    num = bin_int[temp]
                    code += str(num)
                    break

                else:
                    if len(code) == 0:
                        zero_cnt = 0
                        start_dict = {'01101': 0, '011001': 1, '010011': 2, '01011': 9}
                        temp2 = ''.join(matrix[i][:7])
                        first = temp2
                        while len(first) > 4:
                            if first in start_dict:
                                num = start_dict[first]
                                code += str(num)
                                while zero_cnt:
                                    matrix[i] = '0' + ''.join(matrix[i])
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
                    matrix[i] = ''.join(matrix[i]).replace('00', '0')
                    matrix[i] = ''.join(matrix[i]).replace('11', '1')
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