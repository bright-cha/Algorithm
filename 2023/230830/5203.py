def check_win_p1(idx):
    if p1.count(p1[idx]) >= 3:
        print(f'#{tc}', 1)
        return True
    elif (p1[idx] - 1 in p1 and p1[idx] - 2 in p1) or (p1[idx] - 1 in p1 and p1[idx] + 1 in p1) or (p1[idx] + 1 in p1 and p1[idx] + 2 in p1):
        print(f'#{tc}', 1)
        return True
    else:
        if 9 in p1 and 0 in p1:
            if 1 in p1 or 8 in p1:
                print(f'#{tc}', 1)
                return True


def check_win_p2(idx):
    if p2.count(p2[idx]) >= 3:
        print(f'#{tc}', 2)
        return True
    elif (p2[idx] - 1 in p2 and p2[idx] - 2 in p2) or (p2[idx] - 1 in p2 and p2[idx] + 1 in p2) or (p2[idx] + 1 in p2 and p2[idx] + 2 in p2):
        print(f'#{tc}', 2)
        return True
    else:
        if 9 in p2 and 0 in p2:
            if 1 in p2 or 8 in p2:
                print(f'#{tc}', 2)
                return True


T = int(input())
for tc in range(1, T + 1):
    nums = list(map(int, input().split()))

    p1 = []
    p2 = []
    for i in range(6):
        p1.append(nums[i * 2])
        if i >= 2 and check_win_p1(i):
            break

        p2.append(nums[i * 2 + 1])
        if i >= 2 and check_win_p2(i):
            break
    else:
        print(f'#{tc}', 0)
