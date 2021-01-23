nums = [int(el) for el in input().split(', ')]

even = [index for index in range(len(nums)) if nums[index] % 2 == 0]
print(even)
