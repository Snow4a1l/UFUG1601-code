#recursion
#斐波那契

a=str(input('Enter a string: '))


result=0
def f(n):
    if n==1 or n==2:
        result=1
    else:
        result=f(n-1)+f(n-2)
    return result

def convert(n):
    if n==0:
        return '0'
    elif n==1:
        return '1'
    else:
        return convert(n//2)+str(n%2)
    
def bad(n):
    if n==1:
        return 1
    return bad(1+n/2)

def c(n):
    if n==1:
        return 1
    return c(n-1)+ 1.0/n

def hano_tower(num, origin, receive, middle):
    if num==1:
        print(origin, '->', receive)
    else:
        hano_tower(num-1, origin, middle, receive)
        print(origin, '->', receive)
        hano_tower(num-1, middle, receive, origin)




print(hano_tower(3, 'A', 'B', 'C'))