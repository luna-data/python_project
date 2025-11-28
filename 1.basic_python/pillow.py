from PIL import Image
img = Image.open("dog.jpg") # 이미지 열기
img.thumbnail((200, 200)) # 이미지 크기 조절
img.save("thumbnail.jpg") # 조절된 이미지 저장