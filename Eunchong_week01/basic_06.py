s = input("문자열 입력: ")

s_clean = ""
for ch in s:
    if ch != " ":
        s_clean += ch

if s_clean == s_clean[::-1]:
    print("회문입니다")
else:
    print("회문이 아닙니다")