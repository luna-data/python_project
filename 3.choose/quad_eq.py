import math
# 2차 방정식의 계수 입력 받기
a = float(input("2차 방정식의 계수 a를 입력하세요: "))
b = float(input("2차 방정식의 계수 b를 입력하세요: "))
c = float(input("2차 방정식의 계수 c를 입력하세요: "))
# 판별식 계산
discriminant = b**2 - 4*a*c
# 근 계산 및 출력
if discriminant > 0:
# 서로 다른 두 개의 실근
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    print("서로 다른 두 개의 실근이 있습니다:")
    print("근 1:", root1)
    print("근 2:", root2)
elif discriminant == 0:
    pass # pass는 파이썬에서 빈 블록을 나타내는 문장이다.
else:
    pass