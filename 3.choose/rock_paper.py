import random

user=input("가위,바위,보 중 하나를 선택하세요: ")

choices=["가위","바위","보"]
com_choice=random.choice(choices)

print("사용자 선택: ",user)
print("컴퓨터 선택: ", com_choice)

if user==com_choice:
  print("무승부입니다!")

elif (user=="가위" and com_choice=="보")or(user=="바위" and com_choice=="가위")or(user=="보"and com_choice=="바위"):
  print("사용자가 이겼습니다!")
else:
  print("컴퓨터가 이겼습니다!")
