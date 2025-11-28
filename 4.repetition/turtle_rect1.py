import turtle
t = turtle.Turtle()
length = 100
colors = ["red", "green", "blue", "orange", "purple"]
t.width(5) # 5픽셀로 두껍게 설정
for i in range(18): # 18번 반복한다.
    t.left(20) # 왼쪽으로 20도 회전한다.
    t.color(colors[i%5])
    t.forward(length) # length 픽셀 전진한다.
    t.left(90)
    t.forward(length) # length 픽셀 전진한다.
    t.left(90)
    t.forward(length) # length 픽셀 전진한다.
    t.left(90)
    t.forward(length) # length 픽셀 전진한다.
    t.left(90)
# 그래픽 창 유지
turtle.done()