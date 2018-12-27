#brute force approach

def checkprime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
y=1
a=[]
x=0
while(True):
    if checkprime(y):
        a.append(y)
        x+=1
    y+=1
    if(x==10001):
        break

print(a[-1])
print(len(a))


#-------------------------------------------------------------------------------------------------------------#
#efficient
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
y=1    
a=[]
x=0
while(True):
    y+=1
    if checkprime(y):
        a.append(y)
        x+=1
    if(x==10001):
        break
print(a[-1])
