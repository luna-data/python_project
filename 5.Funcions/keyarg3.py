def process_order(customer_name, product, address=None, payment_method=None):
  print(f"{customer_name}님의 주문이 처리되었습니다.")
  print(f"주문 내역 : {product}")

  if address:
    print(f"배송 주소 : {address}")

  if payment_method:
    print(f"결제 방법 : {payment_method}")

process_order("Kim", "사과", address = "서울시 강남구", payment_method = "신용카드")