def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    max_value = max(numbers)
    min_value = min(numbers)
    return total, average, max_value, min_value

numbers = []
while True:
    num = input("숫자를 입력하세요 (종료는 q) : ")
    if num.lower() == 'q':
        break
    numbers.append(int(num))

total, average, max_value, min_value = calculate_stats(numbers)
print("숫자들의 합계 : ", total)
print("숫자들의 평균 : ", average)
print("숫자들의 최댓값 : ", max_value)
print("숫자들의 최솟값 : ", min_value)
