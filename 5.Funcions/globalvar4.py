s = "사과가 좋음!"

def sub():
  global s
  print(s)
  s = "메론이 좋음!"
  print(s)

sub()
print(s)