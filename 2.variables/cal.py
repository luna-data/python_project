# 복리 계산 프로그램

# 사용자 입력 받기
init_money = float(input("초기 금액을 입력하세요: "))
interest = float(input("이자율을 입력하세요(예: 0.06): "))
years = int(input("연수를 입력하세요: "))

# 복리 계산
result = init_money * (1 + interest) ** years

# 결과 출력
print("\n=== 계산 결과 ===")
print(f"초기 금액: {init_money}")
print(f"이자율: {interest}")
print(f"기간(년): {years}")
print(f"최종 금액: {result:.10f}")