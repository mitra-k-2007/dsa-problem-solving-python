a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 4, 5, 6]
p=0
j=0
result=[]
l1=len(a)
l2=len(b)
while p<l1 and j<l2:
    if a[p]>b[j]:
        if not result and result[-1]!=a[p]:
             result.append(a[p])
        p+=1
    elif a[p]<b[j]:
        if not result and result[-1]!=b[j]:
            result.append(b[j])
        j+=1
    else:
        if not result and result[-1]!=a[p]:
            result.append(a[p])
        p+=1
        j+=1
while p<l1:
    if not result and result[-1]!=a[p]:
        result.append(a[p])
    p+=1
while j<l2:
    if not result and result[-1]!=b[j]:
        result.append(b[j])
    j+=1
print(result)
               
        
