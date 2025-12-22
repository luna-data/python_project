class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        total = 0
        for s in self.scores:
            total += s
        return total / len(self.scores)


class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        if not self.students:
            return 0
        total = 0
        for stu in self.students:
            total += stu.average()
        return total / len(self.students)

    def top_student(self):
        if not self.students:
            return None
        best = self.students[0]
        for i in range(1, len(self.students)):
            if self.students[i].average() > best.average():
                best = self.students[i]
        return best

    def pass_rate(self, threshold=60):
        if not self.students:
            return 0
        passed = 0
        for stu in self.students:
            if stu.average() >= threshold:
                passed += 1
        return passed / len(self.students)


# 사용 예시
s1 = Student("철수", [80, 90, 70])
s2 = Student("영희", [50, 60, 55])
s3 = Student("민수", [95, 90, 100])

gb = GradeBook()
gb.add_student(s1)
gb.add_student(s2)
gb.add_student(s3)

print("반 평균:", round(gb.class_average(), 2))

top = gb.top_student()
print("최고 점수 학생:", top.name, round(top.average(), 2))

rate = gb.pass_rate(60)
print("합격률:", round(rate * 100, 1), "%")
