def mean_std(nums):
    n = len(nums)
    total = 0
    for x in nums:
        total += x
    mean = total / n

    var_sum = 0
    for x in nums:
        var_sum += (x - mean) ** 2
    var = var_sum / n
    std = var ** 0.5
    return mean, std

def z_scores(nums):
    mean, std = mean_std(nums)
    zs = []
    for x in nums:
        zs.append((x - mean) / std)
    return zs

data = [50, 60, 70, 80, 90]
zs = z_scores(data)

for i in range(len(data)):
    print("값:", data[i], "z-score:", round(zs[i], 3))
