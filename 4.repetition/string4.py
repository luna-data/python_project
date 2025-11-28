original=input("문자열을 입력하시오:")
word=original.lower()

if len(original)>0 and original.isalpha():

    for index,char in enumerate(word):
        if char in 'aeiou':
            print(f"모음'{char}'이(가) {index}번째 위치에 있습니다.")
        else:
            print(f"자음'{char}'이(가) {index}번째 위치에 있습니다.")