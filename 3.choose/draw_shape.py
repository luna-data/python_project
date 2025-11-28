import turtle
shape = input("어떤 도형을 그리시겠습니까? (원/사각형/삼각형): ")
if shape == "원":
    radius = int(input("반지름을 입력하세요: "))
    turtle.circle(radius)

elif shape == "사각형":
    width = int(input("가로 길이를 입력하세요: "))
    height = int(input("세로 길이를 입력하세요: "))
    for i in range(2): # 2번 반복
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
elif shape == "삼각형":
    length = int(input("한 변의 길이를 입력하세요: "))
    for i in range(3): # 3번 반복
        turtle.forward(length)
        turtle.right(120)
else:
    print("지원하지 않는 도형입니다.")
    turtle.done()