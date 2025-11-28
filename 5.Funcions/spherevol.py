import math

def sphereVolume(radius):
  volume = (4.0/3.0) * math.pi * radius ** 3
  return volume

# 구의 반지름 입력 받기
radius = float(input("구의 반지름을 입력하시오 : "))

# 구의 부피 구하는 함수 호출 및 결과 출력
print("구의 부피 : ", sphereVolume(radius))