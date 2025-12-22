class TodoItem:
    def __init__(self, title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, title):
        item = TodoItem(title)
        self.items.append(item)

    def show_items(self):
        for i in range(len(self.items)):
            item = self.items[i]
            status = "완료" if item.done else "미완료"
            print(i, item.title, "-", status)

    def mark_done(self, index):
        if 0 <= index < len(self.items):
            self.items[index].mark_done()
        else:
            print("잘못된 인덱스입니다.")

# 사용 예시
todo = TodoList()
todo.add_item("파이썬 공부하기")
todo.add_item("데이터 분석 과제하기")
todo.add_item("운동하기")

todo.mark_done(1)
todo.show_items()
