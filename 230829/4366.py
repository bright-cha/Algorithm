T = int(input())
for tc in range(1, T + 1):
    bin_num = input()
    thr_num = input()
    candidates_bin = []
    candidates_thr = []
    for i in range(len(bin_num)):
        temp = list(bin_num)
        if bin_num[i] == '1':
            temp[i] = '0'
            new_num = ''.join(temp)
            candidates_bin.append(int(new_num, 2))
        else:
            temp[i] = '1'
            new_num = ''.join(temp)
            candidates_bin.append(int(new_num, 2))
    for i in range(len(thr_num)):
        temp = list(thr_num)
        if thr_num[i] == '1':
            temp[i] = '0'
            new_num = ''.join(temp)
            candidates_thr.append(int(new_num, 3))

            temp[i] = '2'
            new_num = ''.join(temp)
            candidates_thr.append(int(new_num, 3))
        elif thr_num[i] == '2':
            temp[i] = '1'
            new_num = ''.join(temp)
            candidates_thr.append(int(new_num, 3))

            temp[i] = '0'
            new_num = ''.join(temp)
            candidates_thr.append(int(new_num, 3))
        else:
            temp[i] = '1'
            new_num = ''.join(temp)
            candidates_thr.append(int(new_num, 3))

            temp[i] = '2'
            new_num = ''.join(temp)
            candidates_thr.append(int(new_num, 3))

    for i in candidates_thr:
        if i in candidates_bin:
            print(f'#{tc}', i)