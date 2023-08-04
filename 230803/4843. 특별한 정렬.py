T = int(input())
for tc in range(1, T + 1):
    nums_length = int(input())
    nums = list(map(int, input().split()))

    # 선택정렬
    for i in range(nums_length - 1):
        # 1. i가 홀수 인덱스라면 실행하는 if문
        if i % 2:
            # 1-1) 최소값 i로 저장
            min_idx = i
            for j in range(i + 1, nums_length):
                # 1-2) i 다음 인덱스부터 마지막 값까지 비교하며 최소값을 i에 저장
                if nums[min_idx] > nums[j]:
                    min_idx = j

            # 1-3) 구해진 최소값과 i번째 인덱스의 값을 교환
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

        # 2. i가 홀수 인덱스가 아니라면 => 짝수라면 실행하는 if문
        else:
            # 2-1) 최대값 i로 저장
            max_idx = i
            for j in range(i + 1, nums_length):
                # 2-2) i 다음 인덱스부터 마지막 값까지 비교하며 최대값을 i에 저장
                if nums[max_idx] < nums[j]:
                    max_idx = j

            # 2-3) 구해진 최대값과 i번째 인덱스의 값을 교환
            nums[i], nums[max_idx] = nums[max_idx], nums[i]

    print(f'#{tc} {" ".join(map(str, nums[:10]))}')