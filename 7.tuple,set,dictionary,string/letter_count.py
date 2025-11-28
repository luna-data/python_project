string = input("문자열을 입력하세요 : ")

countTable = {}
for letter in string :
    countTable[letter] = countTable.get(letter, 0) + 1

print(countTable)