nums = [1, 1, 2, 2, 3, 4, 4]

l = 0

for r in range(1, len(nums)):
    if nums[l] != nums[r]:
        l += 1
        nums[l] = nums[r]

print(nums[:l+1])