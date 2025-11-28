#4칙연산이 가능한 계산기를 만들어보자
#2개의 정수를 받아서 더하기, 빼기, 곱하기, 나누기 등을 계산한디
x = int(input("첫 번째 정수를 입력하시오: ")) # 문자열을 정수로 변환한다.
y = int(input("두 번째 정수를 입력하시오: ")) # 문자열을 정수로 변환한다.
result = x + y
print(f"{x}+{y}={result}")
result = x - y
print(f"{x}-{y}={result}")
result = x * y
print(f"{x}*{y}={result}")
result = x / y
print(f"{x}/{y}={result}")