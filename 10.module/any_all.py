def check_all_numeric(string):
    return all(char.isdigit() for char in string)

def check_any_numeric(string):
    return any(char.isdigit() for char in string)

user_input = input("문자열을 입력하세요 : ")

is_all_numeric = check_all_numeric(user_input)

if is_all_numeric:
    print(f"입력한 문자열 {user_input}은 모두 숫자로 이루어져 있습니다.")

is_any_numeric = check_any_numeric(user_input)

if is_any_numeric:
    print(f"입력한 문자열 {user_input}은 숫자를 포함하고뮤 있습니다.")