"""
문제설명:
클래스를 활용하여 "음식 및 음료 주문 시스템"을 구현해봅시다. 
기본적으로 음식 혹은 음료를 나타내는 기본 클래스를 만들고, 이를 상속받아 다양한 종류의 음식, 음료 메뉴를 만들어봅니다.
시스템은 여러 개의 주문을 받을 수 있어야 합니다. 사용자는 주문하고 싶은 메뉴를 선택하고 수량을 입력합니다.
각 주문의 가격을 합산하여 최종 결제 금액을 출력하는 기능도 구현하세요.
상속과 다형성, 그리고 리스트, 반복문, 조건문 등 파이썬의 기초 문법을 반드시 활용합니다.

입력조건:
- Food, Drink 클래스를 모두 만들어 상속 구조를 구현하고, 음식/음료별 가격 정보를 포함시킵니다.
- 사용자는 반복적으로 주문을 추가하며 각 주문별로 메뉴와 수량을 선택할 수 있습니다.
- 주문이 끝나면 주문 내역과 총합을 출력합니다.

출력조건:
- 주문이 끝나면 각 주문 항목(메뉴명, 수량, 금액)이 출력되어야 하며, 마지막에 총 결제 금액이 출력되어야 합니다.

난이도: ★★★★☆ (중급~상급)

클래스 예시 (속성, 메서드):
- MenuItem (이름, 가격, 주문 설명)
  - get_total_price(수량): 해당 수량에 대한 금액 반환
  - describe(): 메뉴 설명 출력
- Food(MenuItem 상속) (음식 종류)
- Drink(MenuItem 상속) (음료 종류)
- Order (여러 메뉴와 수량 저장, 총액 계산 및 주문 내역 출력)

예시결과:
=== 주문 가능한 메뉴 ===
1. 불고기버거(음식) - 5500원
2. 치킨버거(음식) - 6000원
3. 콜라(음료) - 1500원
4. 사이다(음료) - 1500원

메뉴 번호를 입력하세요 (주문 종료: 0): 1
수량을 입력하세요: 2
'불고기버거' 2개가 추가되었습니다.

메뉴 번호를 입력하세요 (주문 종료: 0): 3
수량을 입력하세요: 1
'콜라' 1개가 추가되었습니다.

메뉴 번호를 입력하세요 (주문 종료: 0): 0

=== 주문 내역 ===
불고기버거(음식) 2개 - 11000원
콜라(음료) 1개 - 1500원

총 결제 금액: 12500원

예시 정답 코드:
"""

class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category  # '음식' 또는 '음료'

    def get_total_price(self, count):
        return self.price * count

    def describe(self):
        print(f"{self.name} ({self.category}) - {self.price}원")

class Food(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price, "음식")

class Drink(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price, "음료")

class OrderItem:
    def __init__(self, menu_item, count):
        self.menu_item = menu_item
        self.count = count

    def get_total(self):
        return self.menu_item.get_total_price(self.count)

    def describe(self):
        print(f"{self.menu_item.name}({self.menu_item.category}) {self.count}개 - {self.get_total()}원")

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, order_item):
        self.items.append(order_item)

    def print_receipt(self):
        print("\n=== 주문 내역 ===")
        for item in self.items:
            item.describe()
        print()
        print(f"총 결제 금액: {self.get_total()}원")

    def get_total(self):
        return sum([item.get_total() for item in self.items])

if __name__ == "__main__":
    menu = [
        Food("불고기버거", 5500),
        Food("치킨버거", 6000),
        Drink("콜라", 1500),
        Drink("사이다", 1500)
    ]
    print("=== 주문 가능한 메뉴 ===")
    for idx, item in enumerate(menu, 1):
        print(f"{idx}. {item.name}({item.category}) - {item.price}원")

    order = Order()
    while True:
        try:
            choice = int(input("\n메뉴 번호를 입력하세요 (주문 종료: 0): "))
        except ValueError:
            print("유효한 숫자를 입력하세요.")
            continue

        if choice == 0:
            break
        if 1 <= choice <= len(menu):
            try:
                count = int(input("수량을 입력하세요: "))
            except ValueError:
                print("수량은 숫자로 입력하세요.")
                continue
            if count < 1:
                print("수량은 1개 이상이어야 합니다.")
                continue
            selected_item = menu[choice - 1]
            order.add_item(OrderItem(selected_item, count))
            print(f"'{selected_item.name}' {count}개가 추가되었습니다.")
        else:
            print("올바른 메뉴 번호를 선택하세요.")

    order.print_receipt()
