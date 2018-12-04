target=99999999999999

def sod(x):
    p=target//x
    return (x*(p*(p+1))*0.5)
    
print(sod(3)+sod(5)-sod(15))
