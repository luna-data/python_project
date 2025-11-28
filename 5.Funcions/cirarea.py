PI = 3.14159265358979

def main():
  radius = float(input("원의 반지름을 입력하시오 : "))
  print("원의 면적 :", circleA(radius))
  print("원의 둘레 :", circleC(radius))

def circleA(radius):
  return PI * radius * radius

def circleC(radius):
  return 2 * PI * radius

main()