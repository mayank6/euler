#basically lattice path problem where we can go in right or down cut the problem in half
#like in 20x20 there can be 20 different ways to put right or down in 40 lattice block
#so, 40C20 will be answer

n=20 #matrix squared
mul=1
div=1
for i in range(n*2,n,-1):
    mul*=i
for i in range(n,0,-1):
    div*=i
print(mul/div)
