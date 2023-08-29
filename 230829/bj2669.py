total_round = int(input())
for _ in range(total_round):
    A_info = list(map(int, input().split()))
    cnt_A = A_info.pop(0)
    B_info = list(map(int, input().split()))
    cnt_B = B_info.pop(0)

    A_info.sort()
    B_info.sort()
    rst = 0
    for i in range(4, 0, -1):
        if rst == 0:
            while i in A_info or i in B_info:
                if i in A_info:
                    A_info.pop()
                else:
                    rst = 1
                    break

                if i in B_info:
                    B_info.pop()
                else:
                    rst = 2
                    break

    if rst == 0:
        print('D')
    elif rst == 1:
        print('B')
    else:
        print('A')