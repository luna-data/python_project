prices = [100, 200, 300, 400]
quantities = [2, 3, 5, 1]

total_prices = [price * quantity for price, quantity in zip(prices, quantities)]

print("물건의 총 가격 = ", sum(total_prices))