#물건값 계산,. 구입액이 10만원 이상이면 5%의 할인 해줌
sales = int(input("구입 금액을 입력하시오: "))
if sales>=100000:
  discount = int(sales*0.05)
  sales=sales-discount
else:
  print(100000-sales,"원을 추가 구매하시면 5%할인이 가능합니다")

print("지불 금액은",sales,"원 입니다.")