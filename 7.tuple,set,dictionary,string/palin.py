string = input("문자열을 입력하시오 : ")

reversed_string = string[::-1]

if string == reversed_string:
  print("회문입니다.")
else :
  print("회문이 아닙니다.")