# Angeli Pinol
# Kattis Assignment - Tarifa
# Prof. Johnson
def availMeg():
# The first line of input contains the integer X (1 <= X <= 100).
    mG = int(input())
    x = mG
# Second line of input contains integer N (1 <= N <= 100) 
    n = int(input())
    for i in range(n):
# number of megabytes spent in the first "n" months of using plan
        p = int(input())
        x=x-p+mG

    print(x) # print megabytes available
availMeg()
    
    
