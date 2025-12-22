def summary_stats(nums):
    n = len(nums)
    sorted_nums = sorted(nums)

    # 평균
    total = 0
    for x in nums:
        total += x
    mean = total / n

    # 중앙값
    if n % 2 == 1:
        median = sorted_nums[n // 2]
    else:
        median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2

    # 최소/최대
    min_val = sorted_nums[0]
    max_val = sorted_nums[-1]

    # 분산, 표준편차 (모집단)
    var_sum = 0
    for x in nums:
        var_sum += (x - mean) ** 2
    var = var_sum / n
    std = var ** 0.5

    return {
        "mean": mean,
        "median": median,
        "min": min_val,
        "max": max_val,
        "std": std,
    }

data = [1, 2, 3, 4, 5, 6, 7]
stats = summary_stats(data)
print(stats)
