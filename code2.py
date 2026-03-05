nums = tuple(input("Enter numbers: ").split())

total = 0
for n in nums:
    total = total + int(n)
average = total / len(nums)

print("Average:", average)