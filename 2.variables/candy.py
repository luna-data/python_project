#5000원이 있고 사탕의 가격이 120원이라고 하자
#최대한 살 수 있는 사탕의 개수와 나머지 돈은 얼마인가?
myMoney = 5000
candyPrice = 120
numCandies = myMoney//candyPrice # 최대한 살 수 있는 사탕 수
print(numCandies)
change = myMoney % candyPrice # 최대한 사탕을 구입하고 남은 돈
print(change)