import turtle
t = turtle.Turtle() # 터틀 객체 생성
t.width(5) # 5 픽셀로 두껍게 설정
t.color("blue") # 파란색으로 설정
num_sides = 5 # 다각형을 그릴 때 사용할 변의 개수
side_length = 200 # 다각형의 한 변의 길이
angle = (360.0 / num_sides)*2 # 다각형 내각을 구하기 위해 회전해야 하는 각도
# num_sides에 지정된 개수만큼 반복하여 다각형 그리기
for i in range(num_sides) :
    t.forward(side_length) # side_length만큼 앞으로 이동
    t.right(angle) # angle만큼 오른쪽으로 회전
turtle.done()