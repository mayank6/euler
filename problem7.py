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
