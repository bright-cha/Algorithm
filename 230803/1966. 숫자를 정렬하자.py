T = int(input())
for tc in range(1, T + 1):
    nums_length = int(input())
    nums = list(map(int, input().split()))

    # # 선택정렬
    # for i in range(nums_length - 1):
    #     min_v = i
    #     for j in range(i+1, nums_length):
    #         if nums[min_v] > nums[j]:
    #             min_v = j
    #     nums[min_v], nums[i] = nums[i], nums[min_v]

    # 버블정렬
    for i in range(nums_length - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]

    print(f'#{tc}', *nums)