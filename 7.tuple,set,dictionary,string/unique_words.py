def count_unique_words(text):
  words = text.split()
  unique_words = set(words)

  return len(unique_words)

user_input= input("문자열을 입력하세요 : ")

result = count_unique_words(user_input)
print("중복되지 않은 단어의 개수 : ", result)