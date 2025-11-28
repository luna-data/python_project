word1 = input('첫 번째 단어를 입력해주세요: ')
word2 = input('두 번째 단어를 입력해주세요: ')
word3 = input('세 번째 단어를 입력해주세요: ')
acronym = word1[0] + word2[0] + word3[0]
print(acronym)

#도전문제
word=input("첫번째 단어를 입력해주세요: ")
print(f"첫 번째 문자는 {word[0]}입니다.")
print(f"마지막 문자는 {word[-1]}입니다.")

length=len(word)//2
print(f"가운데 문자는 {word[length]}입니다 ")