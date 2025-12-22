total = 0

while True:
    n = int(input("정수 입력 (0 입력 시 종료): "))
    if n == 0:
        break
    total += n

print("합계:", total)
