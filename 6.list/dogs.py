dogNames = []

while True:
    name = input("강아지의 이름을 입력하시오 (종료 시에는 엔터 키) : ")
    if name == "":
        break
    dogNames.append(name)

print("강아지들의 이름 : ")
for name in dogNames:
    print(name, end= ", ")