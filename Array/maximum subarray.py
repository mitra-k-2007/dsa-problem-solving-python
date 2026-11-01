class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current=nums[0]
        maxi=nums[0]
        for i in range(1,len(nums)):
            current=max(nums[i],current+nums[i])
            maxi=max(current,maxi)
        return maxi
        