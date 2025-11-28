age=int(input("나이를 입력하세요: "))
has_membership=input("회원 여부를 입력하세요(Y/N): ").upper()=="Y"
points=int(input("포인트를 입력하세요: "))

if age>=18 and has_membership and points >=100:
    print("VIP")
elif age>=18 and has_membership:
    print("일반 회원입니다.")
else:
    print("회원이 아닙니다.")