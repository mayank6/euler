def gcd(a,b):
    if (b==0):
        return a
    return gcd(b,a%b)

def lcm(a,b):
    x=a*b/gcd(a,b)
    return x
ans=1
for i in range(2,100):
    ans=lcm(ans,i)
print(ans)
