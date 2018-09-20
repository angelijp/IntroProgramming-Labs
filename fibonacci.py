# CMPT120L-113
# Author: Angeli Pinol

# Intro Message

print("This Program is to display the 'nth' number in the Fibonacci Sequence.")

def fib(n):
    if n == 1:
        return(1)
    elif n == 0:
        return(0)
    else:
        return fib(n-1) + fib(n-2)
    
num = int(input("Enter a number: " ))
print(fib(num))
print("This is the 'nth' term of the Fibonacci Sequence")
