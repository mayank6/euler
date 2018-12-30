def countChain(n):
    if n==1:
        return 1
    if n%2==0:
        return 1+countChain(n/2)
    else:
        return 1+countChain(3*n+1)
l=0
answer=-1

for i in range(1000000):
    if countChain(i)>l:
        l=countChain
        answer=i
print(l,answer)
