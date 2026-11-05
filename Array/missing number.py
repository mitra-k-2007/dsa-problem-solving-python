class Solution(object):
    def missingNumber(self, nums):
       missing=0
       n=len(nums)
       sum_nums=(n*(n+1))/2
       total=sum(nums)
       missing=sum_nums-total
       return missing