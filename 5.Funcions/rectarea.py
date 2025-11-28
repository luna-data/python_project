# 사각형 넓이 계산 함수
def area(w,h):
  return w*h

# 양수 입력을 받는 함수
def input_pos(msg):
  while True:
    value = int(input(msg))
    if value > 0:
      return value
    else:
      print("양수만 입력하시오.")

# 사용자로부터 가로, 세로 길이 입력받기
width = input_pos("사각형의 가로 : ")
height = input_pos("사각형의 세로 : ")

# 면적 계산, 출력하기
result = area(width, height)
print("면적 =", result)