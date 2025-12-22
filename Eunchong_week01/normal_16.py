def safe_int_input(prompt):
    while True:
        s = input(prompt)
        try:
            n = int(s)
            return n
        except ValueError:
            print("정수가 아닙니다. 다시 입력해주세요.")

a = safe_int_input("정수 a: ")
b = safe_int_input("정수 b: ")
c = safe_int_input("정수 c: ")

print("합:", a + b + c)
