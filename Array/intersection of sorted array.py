nums1 = [1, 2, 2, 3, 4, 5]
nums2 = [1, 2, 3, 4]

set2 = set(nums2)
result = []

for num in nums1:
    if num in set2 and num not in result:
        result.append(num)

print(result)