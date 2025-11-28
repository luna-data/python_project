month=int(input("월을 입력하시오: "))

if month==2:
  day=29
elif month==4 or month==6 or month==9 or month==11:
  day=30
else:
  day=31

print("월의 날수는",day)