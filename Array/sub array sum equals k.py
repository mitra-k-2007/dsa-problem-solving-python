class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum=0
        count=0
        freq={0:1}
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            rem=prefix_sum-k
            if rem in freq:
                count+=freq[rem]
            freq[prefix_sum]=freq.get(prefix_sum,0)+1
        return count
        