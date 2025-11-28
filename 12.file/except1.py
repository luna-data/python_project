(x,y)=(2,)
try:
    z=x/y

except ZeroDivisionError as e:
    print("0으로 나누는 예외")