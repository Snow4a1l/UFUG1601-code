a=int(input())
if a>=21:
    print("You are eligible to vote.")
elif a<=20 and a>=13:
    print("You are a teenager.")
elif a<13 and a>=0:
    print("You are a child.")
elif a<0:
    print("Invalid age entered.")