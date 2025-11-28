import turtle
t = turtle.Turtle() # 터틀 객체 생성
num_sides = 6 # 다각형의 변의 개수
side_length = 70 # 다각형의 변의 길이
# 다각형의 내각을 구하기 위해 회전해야 하는 각도
angle = 360.0 / num_sides
# num_sides에 지정된 개수만큼 반복하여 다각형 그리기
for i in range(num_sides):
    t.forward(side_length) # side_length만큼 앞으로 이동
    t.right(angle) # angle만큼 오른쪽으로 회전
turtle.done()