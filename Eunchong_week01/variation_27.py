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
            return True
        else:
            print(self.owner, "계좌 잔액 부족")
            return False

    def show_balance(self):
        print(f"예금주: {self.owner}, 잔액: {self.balance}원")


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print(self.owner, "계좌에 이자", interest, "원 추가")


def transfer(from_acc, to_acc, amount):
    print("=== 계좌 이체 시도 ===")
    ok = from_acc.withdraw(amount)
    if ok:
        to_acc.deposit(amount)
        print("이체 성공")
    else:
        print("이체 실패")


# 사용 예시
acc1 = SavingsAccount("이덕성", 100000)
acc2 = BankAccount("김데사", 20000)

acc1.add_interest(5)  # 5% 이자
transfer(acc1, acc2, 30000)

acc1.show_balance()
acc2.show_balance()
