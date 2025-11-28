def FtoC(temp_f) :
  temp_c = (5.0*(temp_f - 32.0)) / 9.0
  return temp_c

temp_f = float(input("화씨 온도를 입력하시오 : "))

print(FtoC(temp_f))