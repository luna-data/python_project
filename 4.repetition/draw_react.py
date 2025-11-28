import turtle
turtle.speed(0) # 거북이의 속도를 가장 빠른 속도로 설정합니다.
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for color in colors:
    turtle.color(color) # 거북이의 펜 색상을 리스트의 각 색상으로 설정합니다.
    turtle.begin_fill() # 색상으로 채우기를 시작합니다.
    for _ in range(4):
        turtle.forward(100) # 거북이가 100만큼 앞으로 이동합니다.
        turtle.right(90) # 거북이가 90도 오른쪽으로 회전합니다.
    turtle.end_fill() # 색상으로 채우기를 종료합니다.
    turtle.right(60) # 거북이가 60도 오른쪽으로 회전합니다.
turtle.done() # 거북이 그래픽을 종료합니다.