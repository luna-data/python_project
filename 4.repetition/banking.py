#계좌번호 예제
raw=input("계좌번호를 입력하시오: ")
processed=''

for c in raw:
    if c!="-":
        processed=processed+c

print(processed)