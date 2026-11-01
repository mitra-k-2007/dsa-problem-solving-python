nums = [1, 2, 3, 4, 5]

s1 = nums[0]

for i in range(1, len(nums)):
    nums[i-1] = nums[i]

nums.pop()
nums.append(s1)

print(nums)