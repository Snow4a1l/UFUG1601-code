def Factorial(b):
    if b==0 or b==1:
        return 1
    else:
        return b*Factorial(b-1)

print(Factorial(5))


