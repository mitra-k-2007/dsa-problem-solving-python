class Solution(object):
    def moveZeroes(self, nums):
        i=-1
        for k in range(len(nums)):
            if nums[k]==0:
                i=k
                break
        if i==-1:
            return i+1
        for j in range(i+1,len(nums)):
                if nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
        