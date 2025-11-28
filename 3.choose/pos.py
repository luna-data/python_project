#팁 결정하기
price=float(input("음식 값 입력"))
print("팁을 선택하세요:")
print("1. 10%")
print("2. 15%")
print("3. 20%")

tip=input("팁 선택(1/2/3): ")

if tip==1:
  tip=float(10)
elif tip==2:
  tip=float(15)
elif tip==3:
  tip=float(20)
else:
  tip=float(15)

t_price=price*tip*0.01
total_price=price+t_price

print("음식값: $",price)
print("선택한 팁:", tip,"%")
print("팁 금액: $",t_price)
print("총 지불 금액: $", total_price)

#소수점 오류
print(f"음식 값: ${price:.2f}")
print(f"선택한 팁: {tip*0.01}%")
print(f"팁 금액: ${t_price:.2f}")
print(f"총 지불 금액: ${total_price:.2f}")