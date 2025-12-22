class TodoItem:
    def __init__(self, title, category):
        self.title = title
        self.category = category
        self.done = False

    def mark_done(self):
        self.done = True


class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, title, category):
        item = TodoItem(title, category)
        self.items.append(item)

    def show_items(self):
        for i in range(len(self.items)):
            item = self.items[i]
            status = "완료" if item.done else "미완료"
            print(i, item.title, "/", item.category, "-", status)

    def mark_done(self, index):
        if 0 <= index < len(self.items):
            self.items[index].mark_done()
        else:
            print("잘못된 인덱스입니다.")

    def category_stats(self):
        stats = {}  # {카테고리: [전체, 완료]}
        for item in self.items:
            if item.category not in stats:
                stats[item.category] = [0, 0]
            stats[item.category][0] += 1
            if item.done:
                stats[item.category][1] += 1

        result = {}
        for cat in stats:
            total = stats[cat][0]
            done = stats[cat][1]
            result[cat] = (total, done)
        return result


# 사용 예시
todo = TodoList()
todo.add_item("파이썬 과제 하기", "공부")
todo.add_item("통계 복습하기", "공부")
todo.add_item("러닝 30분 하기", "운동")
todo.add_item("방 청소하기", "집안일")

todo.mark_done(0)
todo.mark_done(2)

todo.show_items()
print("카테고리 통계:", todo.category_stats())
