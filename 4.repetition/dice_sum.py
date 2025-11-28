from random import randint

count=int(input("주사위 실험 반복횟수: "))
sum_count=[0,0,0,0,0,0,0,0,0,0]

for i in range(count):
    die1=randint(1,6)
    die2=randint(1,6)
    sum_count[die1+die2-2]+=1

for i in range(2,13):
    probability=100*sum_count[i-2]/count
    print(f"주사위 합{i}의 확률:{probability}%")
