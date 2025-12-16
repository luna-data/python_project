# 문제 1: 자동차(Car) 클래스를 작성하고 객체를 생성해보세요.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year}년식 {self.brand} {self.model}")

car1 = Car("Hyundai", "Sonata", 2022)
car1.display_info()

# 문제 2: 원(Circle) 클래스를 만들고, 넓이와 둘레를 구하는 메서드를 추가해보세요.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14159 * self.radius * self.radius

    def get_circumference(self):
        return 2 * 3.14159 * self.radius

circle1 = Circle(5)
print("원의 넓이:", circle1.get_area())
print("원의 둘레:", circle1.get_circumference())

# 문제 3: 가전제품(Electronic) 클래스를 상속받는 TV 클래스와, 동적 메서드 오버라이딩 예제를 구현해보세요.
class Electronic:
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        print(f"{self.name}의 전원을 켭니다.")

class TV(Electronic):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def turn_on(self):
        print(f"{self.size}인치 {self.name} TV를 켭니다.")

tv1 = TV("삼성", 55)
tv1.turn_on()
# 문제 4: 가전제품(Electronic) 클래스를 추상 클래스로 만들고, 
# 이를 상속하는 TV, Refrigerator, Washer 클래스를 만들어 각각 turn_on() 메서드를 오버라이딩하세요.
# 그리고 다양한 인스턴스를 리스트에 담아 for문으로 turn_on()을 호출해 보세요.

from abc import ABC, abstractmethod

class ElectronicAbstract(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def turn_on(self):
        pass

class TV2(ElectronicAbstract):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def turn_on(self):
        print(f"{self.size}인치 {self.name} TV의 전원을 켭니다.")

class Refrigerator(ElectronicAbstract):
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity

    def turn_on(self):
        print(f"{self.name} 냉장고({self.capacity}L)의 전원을 켭니다.")

class Washer(ElectronicAbstract):
    def __init__(self, name, rpm):
        super().__init__(name)
        self.rpm = rpm

    def turn_on(self):
        print(f"{self.name} 세탁기({self.rpm}rpm)의 전원을 켭니다.")

products = [
    TV2("LG", 65),
    Refrigerator("삼성", 500),
    Washer("다이슨", 1200)
]

for product in products:
    product.turn_on()
