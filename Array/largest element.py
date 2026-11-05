class Solution:
    def largestElement(self, nums):
        largest=float('-inf')
        for i in range(len(nums)):
            if nums[i]>largest:
                largest=nums[i]
        return largest