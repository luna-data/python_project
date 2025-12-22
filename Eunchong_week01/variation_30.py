class LabeledPoint:
    def __init__(self, value, label):
        self.value = value
        self.label = label


class LabeledDataset:
    def __init__(self):
        self.points = []

    def add_point(self, value, label):
        p = LabeledPoint(value, label)
        self.points.append(p)

    def mean(self):
        if not self.points:
            return 0
        total = 0
        for p in self.points:
            total += p.value
        return total / len(self.points)

    def mean_by_label(self, label):
        total = 0
        count = 0
        for p in self.points:
            if p.label == label:
                total += p.value
                count += 1
        if count == 0:
            return None
        return total / count

    def std(self):
        m = self.mean()
        if not self.points:
            return 0
        var_sum = 0
        for p in self.points:
            var_sum += (p.value - m) ** 2
        var = var_sum / len(self.points)
        return var ** 0.5

    def z_scores(self):
        m = self.mean()
        s = self.std()
        result = []
        for p in self.points:
            if s == 0:
                z = 0
            else:
                z = (p.value - m) / s
            result.append((p.value, p.label, z))
        return result


# 사용 예시
ld = LabeledDataset()
ld.add_point(10, "A")
ld.add_point(20, "A")
ld.add_point(30, "B")
ld.add_point(40, "B")
ld.add_point(50, "B")

print("전체 평균:", ld.mean())
print("A 그룹 평균:", ld.mean_by_label("A"))
print("B 그룹 평균:", ld.mean_by_label("B"))

zs = ld.z_scores()
for value, label, z in zs:
    print("값:", value, "레이블:", label, "z-score:", round(z, 3))
