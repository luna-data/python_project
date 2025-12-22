line = input("정수 여러 개 입력 (공백으로 구분): ")

parts = line.split()
nums = []

for p in parts:
    nums.append(int(p))

total = 0
for x in nums:
    total += x

avg = total / len(nums)

print("합:", total)
print("평균:", avg)
