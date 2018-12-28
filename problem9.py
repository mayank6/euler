for m in range(1,1000):
    for n in range(m+1,1000):
        sum=0
        for k in range(1000):
            sum=0
            a=n**2-m**2
            b=2*m*n
            c=n**2+m**2
            sum=k*a+k*b+k*c
            if (sum==1000):
                print(k,a,b,c)
                print(a*b*c)
                break
            if(sum>1000):
                break
        
        
