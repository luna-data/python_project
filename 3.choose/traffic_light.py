import turtle
# 터틀 객체 생성
t = turtle.Turtle()
# 신호 입력 받기
signal = input("신호를 입력하세요 (red, yellow, green): ")
# 신호에 따라 원 그리기
if signal == "red":
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.color("green")
    t.goto(100, 100)
    t.circle(50)
    t.color("yellow")
    t.goto(200, 100)
    t.circle(50)
elif signal == "yellow":
    pass # 구현해보자.
elif signal == "green":
    pass # 구현해보자.
else:
    print("지원되지 않는 신호입니다.")
# 터틀 그래픽 종료
turtle.done()