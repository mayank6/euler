def sumdivisor(x):
    s=0
    for i in range(1,int(x/2)+1):
        if x%i==0:
            s+=i
    return s
sum=0
for i in range(2,10000):
    j=sumdivisor(i)
    if j>i:
        if sumdivisor(j)==i: 
            sum=sum+i+j
print(sum)
