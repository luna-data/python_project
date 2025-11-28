numbers = [1, 2, 3, 4, 5]

def is_even(num):
    return num % 2 == 0

def square_number(num):
    return num ** 2

filtered_even_numbers = filter(is_even, numbers)
squared_numbers = map(square_number, filtered_even_numbers)

result_list = list(squared_numbers)

print("입력 리스트 = ", numbers)
print("결과 리스트 = ", result_list)
