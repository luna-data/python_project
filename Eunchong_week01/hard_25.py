class Dataset:
    def __init__(self, data):
        self.data = data

    def mean(self):
        total = 0
        for x in self.data:
            total += x
        return total / len(self.data)

    def std(self):
        m = self.mean()
        var_sum = 0
        for x in self.data:
            var_sum += (x - m) ** 2
        var = var_sum / len(self.data)
        return var ** 0.5

    def summary(self):
        sorted_data = sorted(self.data)
        return {
            "mean": self.mean(),
            "min": sorted_data[0],
            "max": sorted_data[-1],
        }

    def z_scores(self):
        m = self.mean()
        s = self.std()
        zs = []
        for x in self.data:
            zs.append((x - m) / s)
        return zs

data = [10, 20, 30, 40, 50]
ds = Dataset(data)

print("요약:", ds.summary())
zs = ds.z_scores()
for i in range(len(data)):
    print("값:", data[i], "z-score:", round(zs[i], 3))
