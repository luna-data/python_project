def mean(nums):
    total = 0
    for x in nums:
        total += x
    return total / len(nums)

data = [10, 20, 30, 40, 50]
print(mean(data))
