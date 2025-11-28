input_string = input("문자열을 입력하시오 : ")

words = input_string.split()
word_count = {}

for word in words :
  word = word.lower()

  if word not in word_count :
    word_count[word] = 1
  else :
    word_count[word] += 1

for word, count in word_count.items() :
  print(f"'{word}' : {count}번")