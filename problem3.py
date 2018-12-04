import math
def checkprime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
num=600851475143
li=[]
i=2

while i<600851475143:
        if checkprime(i):
            if num%i==0:
                li.append(i)
                num=num/i
            else:
                i+=1
        else:
            i+=1
        if num==1:
            break
print(li)
