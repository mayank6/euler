def pcheck(x):
    y=int(str(x)[::-1])
    if x==y:
        return True
    else:
        return False

# for i in range(100,1000):
#     for j in range(100,1000):
maxi=0
for i in range(100,1000):
    for j in range(100,1000):
        if(pcheck(j*i)):
            if maxi<i*j:
                maxi=i*j
print(maxi)            
