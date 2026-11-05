arr = [2, 1, 2]
k = 3
prefix_Sum=0
max_len=0
mp={0:-1}
for i in range(len(arr)):
    prefix_sum+=arr[i]
    rem=prefix_sum-k
    if rem in mp:
        length=i-mp[rem]
        max_len=max(length,max_len)
    if prefix_sum not in mp:
        mp[prefix_sum]=i
print( max_len)
