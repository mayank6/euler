#inefficient solution
import math
def checkprime(x):
    if x==1:
        return False
    if x==2 or x==3:
        return True
    if x%2==0:
        return False
    if x%3==0:
        return False
    if x<9:
        return True
    if x%3==0:
        return False
    
    k=5
    f=math.floor(math.sqrt(x))
    
    while(k<=f):
        if(x%k==0):
            return False
        if(x%(k+2)==0):
            return False
        k+=6
    return True
sum=0
for i in range(2000000):
    if checkprime(i):
        sum+=i
print(sum)

#---------------------------------------------------------------------------------------------#

