with open('12.file/proverbs.txt','rb')as file:
    file.seek(10,0)

    position=file.tell()
    print("현재 파일 포인터 위치:", position)

    data=file.read(5)
    print("잃은 데이터:",data)