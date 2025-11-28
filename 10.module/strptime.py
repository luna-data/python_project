from datetime import datetime
date_string=input("날짜를 입력하세요 (예: 2023-12-10): ")
try:
    date_object=datetime.strptime(date_string, "%Y-%m-%d")
    print("입력한 날짜 객체:", date_object)
except ValueError:
    print('잘못된 형식의 날짜입니다. 올바른 형식으로 다시 입력하세요.')
    