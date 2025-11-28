# 함수 정의
def sub(mylist):
  mylist = [1, 2, 3, 4]
  print("함수 내부에서의 mylist :", mylist)
  return

# sub 함수 호출
mylist = [10, 20, 30, 40]
sub(mylist)
print("함수 외부에서의 mylist :", mylist)