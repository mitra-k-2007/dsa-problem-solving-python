nums =[10, 22, 12, 3, 0, 6]
maxi=float('-inf')
result=[]
for i in range(len(nums)-1,-1,-1):
    if nums[i]>=maxi:
        result.append(nums[i])
        maxi=nums[i]
result.reverse()
print(result)