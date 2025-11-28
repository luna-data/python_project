keyword_list=[]
user_input=""

while user_input!="quit":
  user_input=input("단어를 입력하세요('quit'으로 종료):")

  if user_input!="quit":
    keyword_list.append(user_input)

keyword_count=len(keyword_list)
print("입력된 단어 개수:",keyword_count)
print("입력된 단어 목록:",keyword_list)