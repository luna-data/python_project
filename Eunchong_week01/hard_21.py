class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        total = 0
        for s in self.scores:
            total += s
        return total / len(self.scores)

    def is_pass(self, threshold=60):
        return self.average() >= threshold

students = [
    Student("철수", [80, 90, 80]),
    Student("영희", [50, 60, 61]),
    Student("민수", [100, 90, 95])
]

for s in students:
    avg = s.average()
    if s.is_pass():
        result = "합격"
    else:
        result = "불합격"
    print(s.name, f"{avg:.1f}", result)
