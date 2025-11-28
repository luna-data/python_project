 # 첫 번째 사각형 입력 받기
print("첫 번째 사각형 좌표를 입력하세요.")
x1 = int(input("왼쪽 상단 x 좌표: "))
y1 = int(input("왼쪽 상단 y 좌표: "))
w1 = int(input("너비: "))
h1 = int(input("높이: "))
# 두 번째 사각형 입력 받기
print("두 번째 사각형 좌표를 입력하세요.")
x2 = int(input("왼쪽 상단 x 좌표: "))
y2 = int(input("왼쪽 상단 y 좌표: "))
w2 = int(input("너비: "))
h2 = int(input("높이: "))
# 겹치지 않는지 검사
if x1 >= x2 + w2 or x1 + w1 <= x2 or y1 >= y2 + h2 or y1 + h1 <= y2:
    print("두 사각형은 겹치지 않습니다.")
else:
    print("두 사각형은 겹칩니다.")