def factorial(n):
  result = 1
  for i in range(1, n+1) :
    result *= i
  return result

number = 5
factorial_result = factorial(number)
print(f"{number}의 팩토리얼은 {factorial_result}입니다.")