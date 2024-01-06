T = int(input())
for tc in range(1, T + 1):
    nums = list(map(int, input().split()))
    rst = 0

    nums_length = len(nums)
    for i in range(1, 1 << nums_length):
        nums_lst = []
        for j in range(nums_length):
            if i & (1 << j):
                nums_lst.append(nums[j])
        if sum(nums_lst) == 0:
            rst = 1

    print(f'#{tc} {rst}')