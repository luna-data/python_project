#근무시간과 시간당 임금을 물어본다. 주당 근무시간 40시간 까지는 기본 임금이고 40시간을 넘는 시간에 대해서는 1.5배의 임금을 지급해야 한다
hours=int(input("근무시간을 입력하시오: "))
wage=int(input("시간당 임금을 입력하시오: "))

if hours<=40:
  totalWages=wage*hours

else:
  hour=hours-40
  totalWages=wage*1.5*hour+(hours-hour)*wage

print(totalWages)