class Dog(Animal):
    def __init__(self):
        super().__init__()
    def eat(self):
        print("강아지가 먹고 있습니다.")

d=Dog()
d.eat()