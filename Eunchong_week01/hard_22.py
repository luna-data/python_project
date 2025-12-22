class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.owner, "계좌에", amount, "원 입금")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(self.owner, "계좌에서", amount, "원 출금")
        else:
            print("잔액 부족")

    def show_balance(self):
        print(f"예금주: {self.owner}, 잔액: {self.balance}원")

# 사용 예시
acc = BankAccount("김데사", 10000)
acc.deposit(5000)
acc.withdraw(3000)
acc.withdraw(20000)
acc.show_balance()
